import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('ramzanblogs.blogspot.com', 443))
cmd = 'GET https://ramzanblogs.blogspot.com/2020/06/scope-of-electric-vehicles-recent.html HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()
print('executed')
