#common commands
CLEAR(ser) 
    ser.write(0xFE) #may need chr(0xFE)
    ser.write(0x51)


