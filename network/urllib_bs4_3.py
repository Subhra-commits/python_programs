import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup
import ssl

#ignore ssl certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

url=input('Enter URL: ')
html=urllib.request.urlopen(url,context=ctx).read()
soup=BeautifulSoup(html,'html.parser')

count_tags=0

#Retrieve all <a> tags
a_tags=soup('a')
for tag in a_tags:
    count_tags=count_tags+1

print('No. of <a> tags are: ',count_tags)
