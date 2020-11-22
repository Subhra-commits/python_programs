import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    URL=input("Enter the URL of your desired webpage: ")
    HOST= URL.split('/')[2]
except:
    print("Error: Improper format or URL doesnot exist")
    quit()

#print(HOST)
mysock.connect((HOST, 80))
cmd = 'GET URL HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()
