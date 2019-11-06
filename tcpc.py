import socket
import timeit
import threading

def run():
    sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sc.connect(('127.0.0.1', 9999))
    sc.send(b'hello server')
    data = sc.recv(1024)
    print(f'recv:{data}')
    sc.close()

def test(n):
    thrs = []
    for i in range(n):
        t = threading.Thread(target=run)
        t.start()
        thrs.append(t)
    for thr in thrs:
        thr.join()

t = timeit.Timer('test(5)', "from __main__ import test")
print(t.timeit(1))