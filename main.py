# Import package
#import paho.mqtt.client as mqtt
import time
import serial
#add logging capability
import logging

import modbus_tk_
import modbus_tk_.defines as cst
import modbus_tk_.modbus_rtu as modbus_rtu

#logger = modbus_tk_.utils.create_logger("console")

master = modbus_rtu.RtuMaster(serial.Serial(port='/dev/ttyO0', baudrate=9600, bytesize=8, parity='N', stopbits=1, xonxoff=0))
master.set_timeout(3.0)
master.set_verbose(True)
a=0
arr = [0,1,2,3,4,5,6,7,8,9,10]
while a<1000:
    data = master.execute(2, cst.READ_HOLDING_REGISTERS, 1000, 8)
    #print data
    time.sleep(0.25)
    for i in range(len(arr)):
        arr[i] = arr[i] + 1
    print arr
    data = master.execute(2, cst.WRITE_MULTIPLE_REGISTERS, 2000, output_value=arr)
    #print data
    time.sleep(0.25)
    a = a + 1

