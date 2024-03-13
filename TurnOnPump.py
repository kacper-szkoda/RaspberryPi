import time
import RPi.GPIO as GPIO
from gpiozero import MCP3008

GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.OUT)
#weight_sensor
weight = MCP3008(0)

def weight_sens():
    print(weight.value)
    time.sleep(1)

while True:
    #GPIO.output(5, True)
    time.sleep(2)
    #GPIO.output(5, False)
    print(MCP3008(0).value)
    print("weight")
    print(MCP3008(4).value)
    print("ldr")
    print(MCP3008(3).value)
    print("moist")


