import urllib.request, urllib.parse,urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count = int(input("Enter count: "))
pos=int(input('Enter position: '))

#n=0
while count>0:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags=soup('a')
    for tag in tags:
        #print(tag.contents[0])
        print(tag.attrs)
    #a_list = soup.find_all(tags[0])
    #print(tags)
    #url=tags[pos-1].get('href',None)
    print('Retrieving: ',url)
    url=tags[pos-1].get('href',None)
    #pos=pos-1
    count=count-1
