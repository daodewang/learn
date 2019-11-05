import socket
sc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
saddr = ('127.0.0.1', 9999)
sc.sendto(b'hello server', saddr)
data, addr = sc.recvfrom(1024)
print(f'recv:{data}')
sc.close()