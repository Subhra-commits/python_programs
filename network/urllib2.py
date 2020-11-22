import urllib.request,urllib.parse, urllib.error
img= urllib.request.urlopen('http://data.pr4e.org/cover3.jpg')

fhand=open('cover3.jpg','wb')
count=list()
size=0
while True:
    info=img.read(10000)
    if len(info)<1:
        break
    size=size+len(info)
    fhand.write(info)

# print(fhand)
'''img1 = info.split('\')
for i in img1:
    count.append(i)
print(count)'''
#print(len(info.encode('utf-8')))
print(size)
fhand.close()
