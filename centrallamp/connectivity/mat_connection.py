from bluepy import btle

mat_addr = "C0:0F:3E:A9:48:2C"

print "Connecting to" + mat_addr
dev = btle.Peripheral(mat_addr)

print "Services"
for svc in dev.services:
    print str(svc)
