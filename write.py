#!/usr/bin/env python
                      
      
import time
import serial
          
print("start")
ser = serial.Serial(port='/dev/ttyAMA0',baudrate = 9600,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=1)
print(" serial start")
counter=0
          
      
while 1:
    ser.write(str.encode("test"))
    print(counter)
    time.sleep(1)
    counter += 1
