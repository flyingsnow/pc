import os
import sys, time
sys.path.append(".\serial")
import serial 
import fileinput

ser = serial.Serial()
ser.baudrate = 115200
ser.port = 'COM7'
ser.open()
ser.write_timeout = 1
# ser.write('led = machine.Pin(25, machine.Pin.OUT)\r'.encode("utf-8"))
# ser.write(b"led.value(1)\r")
# ser.write(b'from machine import Pin, PWM\r')
# ser.write(b'heater = PWM(Pin(9))\r')

# ser.write(b'heater.freq(1000)\r')
# ser.write(b'heater.duty_u16(50000)\r')
for line in fileinput.input(files ='config.txt'):
    line += '\r'
    print(line.encode('utf-8'))
    ser.write(line.encode('utf-8'))

def set_fan_duty(duty):
    cmd = 'fan.duty_u16('+ str(duty) +')\r'
    print(cmd)
    ser.write(cmd.encode('utf-8'))
    print("cmd write done")

def set_heater_duty(duty):
    cmd = 'heater.duty_u16('+ str(duty) +')\r'
    print(cmd)
    ser.write(cmd.encode('utf-8'))
    print("cmd write done")

fan_speed = 24000
while 1:
    # str_out = b'heater.duty_u16('
    # str_out += input("input duty cycle: ").encode('utf-8')
    # str_out += b')\r'
    # print(str_out)
    # ser.write(str_out)

    # temp = int(os.popen('adb shell cat /sys/class/thermal/thermal_zone1/temp').read())
    # temp = int(os.popen('adb shell cat /sys/class/thermal/thermal_zone0/temp').read())
    # print(temp)
    if fan_speed < 65535:
        fan_speed += 100
    else:
        break

    time.sleep(0.5)
    set_fan_duty(fan_speed)
    set_heater_duty(fan_speed)
    print(fan_speed)