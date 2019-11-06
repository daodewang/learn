import socket
import threading
def serveclient(s_client, n):
    s_client.send(b'hello')
    data = s_client.recv(1024)
    if data:
        print(f"client{n} send: {data}")
    s_client.send(b'bye')
    s_client.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 9999))
s.listen(5)
n = 0
print('MT server is working бнбн')
while True:
    s_client, addr_client = s.accept()
    n = n+1
    t = threading.Thread(target=serveclient,
                         args=(s_client, n))
    t.start()