import json
import urllib

from gpiozero import MCP3008
import time

ldr = MCP3008(4)
moist = MCP3008(3)

def addMoisture():
    try:
        with urllib.request.urlopen('https://studev.groept.be/api/a23ib2a01/check_on') as url:
            data = json.load(url)
    except urllib.error.HTTPError as e:
        print("http error")

while True:
    print(ldr.value)
    addMoisture()
    time.sleep(1)
    print(moist.value)
    time.sleep(1)


