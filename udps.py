import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 9999))
while True:
    data, addr = s.recvfrom(1024)
    if data :
        print(f"client send: {data}")
    s.sendto(b'hello, bye', addr)