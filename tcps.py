import socket

DATALEN = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = '127.0.0.1'
port = 9999
s.bind((addr, port))
s.listen(5)
n = 0

while True:
    s_client, addr_client = s.accept()
    n = n+1
    data = s_client.recv(DATALEN)
    if data :
        print(f"client{n} send: {data.decode('utf8')}")

    s_client.send(f'hello, you are No.{n} client, bye'.encode('utf8'))
    s_client.close()
