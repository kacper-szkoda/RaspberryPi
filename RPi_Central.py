import RPi.GPIO as GPIO
from gpiozero import MCP3008
import time
import json
import urllib.request

#pump
GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.OUT)
#weight_sensor
weight = MCP3008(0)

with urllib.request.urlopen('https://studev.groept.be/api/a23ib2a01/check_on') as url:
    data = json.load(url)
    print(data)

print(data[0].get('toggle'))

def weight_sens():
        print(weight.value)
        time.sleep(1)
        with urllib.request.urlopen('https://studev.groept.be/api/a23ib2a01/set_weight/' + weight.value) as url:
            data = json.load(url)

try:
    while True:
        try:
            with urllib.request.urlopen('https://studev.groept.be/api/a23ib2a01/check_control') as url:
                data = json.load(url)
            if int(data[0].get('toggle')) == 1:
                GPIO.output(12, True)
                print('Im on!')
                weight_sens()
                time.sleep(3)
            else:
                GPIO.output(12, False)
                print('im off!')
                weight_sens()
                time.sleep(3)
        except urllib.error.HTTPError as e:
            weight_sens()
            time.sleep(3)
except KeyboardInterrupt:
    print("Programme interrupted")
