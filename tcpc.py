import socket

sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = '127.0.0.1'
port = 9999

sc.connect((addr, port))
sc.send('hello server'.encode('utf8'))
data = sc.recv(1024)
print(f'recv:{data.decode("utf8")}')
sc.close()