from bluepy import btle

panel_addr = "C0:0F:3E:A9:48:2C"

print "Connecting to" + panel_addr
dev = btle.Peripheral(panel_addr)

print "Services"
for svc in dev.services:
    print str(svc)
