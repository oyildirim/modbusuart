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
while a<10:
    data = master.execute(2, cst.READ_HOLDING_REGISTERS, 0, 8)
    time.sleep(0.15)
    data = master.execute(2, cst.WRITE_SINGLE_REGISTER, 0, output_value=1)
    time.sleep(0.15)

