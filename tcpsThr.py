import socket
import threading
import signal


IS_EXIT = False
thrs = []


def signal_handler(signal, frame):
    print('You pressed Ctrl+C!')
    global IS_EXIT
    IS_EXIT = True


def serveclient(s_client, n):
    s_client.send(b'hello')
    data = s_client.recv(1024)
    if data:
        print(f"client{n} send: {data}")
    s_client.send(b'bye')
    s_client.close()


signal.signal(signal.SIGINT, signal_handler)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 9999))
s.listen(5)
s.settimeout(1)
n = 0
print('MT server is working ...')
while True:
    try:
        s_client, addr_client = s.accept()
        n = n+1
        t = threading.Thread(target=serveclient,
                             args=(s_client, n))
        t.start()
        thrs.append(t)
    except socket.timeout:
        if IS_EXIT:
            for t in thrs:
                t.join()
            print('all threads are finished')
            s.close()
            break

