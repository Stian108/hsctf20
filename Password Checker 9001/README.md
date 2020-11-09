# Password Checker 9001
Solves: 6

## Description
A hacker broke into the string theory scientist's computer and left a superior password checking application as a taunt to the scientist. Can you help the poor scientist find out how it works and if it's safe?

## Solution
Start by firing up GDB, by `disass main` we can see that there is a call to `strcmp` at `0x00005555555552ec`, so lets set a breakpoint there and see what is being compared: `b *0x00005555555552ec` and check the string that is being passed to `strcmp` with `x/s $rax` which gives the flag:
```
HSCTF{strings_cant_save_you_this_time_mr_scientist!}
```