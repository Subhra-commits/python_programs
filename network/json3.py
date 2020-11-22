import urllib.request, urllib.parse, urllib.error
import json

while True:
    address= input('Enter location: ')
    if len(address)<1: break
    #url = urllib.parse.urlencode(address)
    print('Retrieving:',address)
    uh = urllib.request.urlopen(address)
    data = uh.read().decode()

    js = json.loads(data)
    sum=0

    for c in (js["comments"]):
        sum+= c["count"]

    print(sum)
