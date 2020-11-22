import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
print('Retrieving:', url) #class str
uh = urllib.request.urlopen(url,context=ctx).read()
#print('2_uh', uh, type(uh)) #class 'http.client.HTTPResponse'
#data = uh.read()
#print("3_uh.read() or data", data, type(data)) #calss bytes
data = uh.decode()
#print("4_data decode", data, type(data)) #class str
tree = ET.fromstring(data)
#print("5_tree", tree, type(tree)) #class 'xml.etree.ElementTree.Element'
count = tree.findall('.//count')
#print("6_count", count, type(count), "len", len(count)) #class 'list
i = 0
#i = int(i)
print(len(count))
Sum = list()
#while True:
for c in count :
    #try :
    countext = count[i].text
    Sum.append(int(countext))
    #print("7_count", countext, type(countext))
    i = i + 1
    #continue
    #except :
    #    break
print("Sum of the numbers is:", sum(Sum))
