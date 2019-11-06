import selectors
import socket


ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.bind(('127.0.0.1', 9999))
ss.listen(5)
n = 0
print('Server is working ……')

sel = selectors.DefaultSelector()
sel.register(ss, selectors.EVENT_READ, data=(-1, -1))

try:
    while True:
        events = sel.select()
        for key, mask in events:
            No, state = key.data
            s = key.fileobj

            if state == -1:
                s_client, addr_client = s.accept()
                n = n+1
                sel.register(s_client, selectors.EVENT_WRITE, data=(n, 0))

            elif state == 0:
                s.send(b'hello')
                sel.modify(s, selectors.EVENT_READ, data=(n, 1))

            elif state == 1:
                data = s.recv(1024)
                if data:
                    print(f"client{n} send: {data}")
                s.send(b'bye')
                s.close()
                sel.unregister(s)
except:
    print('Server closed')
finally:
    sel.close()
    ss.close()

