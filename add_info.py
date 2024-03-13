import json
import urllib.request

with urllib.request.urlopen('https://studev.groept.be/api/a23ib2a01//' + "a" + "/1990-01-01" + "/0.2") as url:
    data = json.load(url)