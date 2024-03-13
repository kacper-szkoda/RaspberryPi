import json
import urllib.request
from gpiozero import MCP3008
import datetime
import time

ldr = MCP3008(4)
moist = MCP3008(3)

name = "lily"

while True:
    time.sleep(5)
    try:
        with urllib.request.urlopen('https://studev.groept.be/api/a23ib2a01/moisture_reading/' + name + '/' + datetime.datetime.now().strftime('%Y-%m-%d') +'/' + str(moist)) as url:
            data = json.load(url)
        with urllib.request.urlopen('https://studev.groept.be/api/a23ib2a01/ldr_reading/' + name + '/' + datetime.datetime.now().strftime('%Y-%m-%d') +'/' + str(ldr)) as url:
            data = json.load(url)
    except KeyboardInterrupt:
        print("interrupt")
