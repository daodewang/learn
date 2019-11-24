import socket
import threading
from blessings import Terminal
from queue import Queue
import simple_blessing as SB


IS_EXIT = False
T = Terminal()
H = T.height
L = H // 3
promote = '>>>'

q_user = Queue(L - 1)
q_recv = Queue(L - 1)
q_send = Queue(L - 2)


def online(writer, reader, addr, port, user):
    global q_recv
    writer.connect((addr, port))
    writer.send(user.encode('utf-8'))

    data = writer.recv(128)
    SB.add2que(q_recv, data.decode("utf-8"))
    SB.updateRecv(T, q_recv, L)

    if data.decode('utf-8')[0:5] == 'hello':

        reader.connect((addr, port))
        reader.send(user.encode('utf-8'))
        data = reader.recv(128)
        if data.decode('utf-8') == 'OK' :
            msg = f'{user} is online, type "bye" to offline'
            SB.add2que(q_recv, msg)
            SB.updateRecv(T, q_recv, L)


def write(writer):
    global IS_EXIT
    while True:
        msg = input('msg>')

        SB.add2que(q_send, msg)
        SB.freshTer(T, q_user, q_recv, q_send, L)
        if IS_EXIT:
            break

        writer.send(msg.encode('utf-8'))

        if msg == 'bye':
            IS_EXIT = True
            break


def main():


    SB.freshTer(T, q_user, q_recv, q_send, L)

    global IS_EXIT
    writer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    reader = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    reader.settimeout(1)
    online(writer, reader, '127.0.0.1', 9999, 'Mike')

    w = threading.Thread(target=write, args=(writer,))
    w.start()

    while True:
        try:
            msg = reader.recv(1024)
            if not msg:
                m = 'server seems closed, type any to exit'
                SB.add2que(q_recv, m)
                SB.updateRecv(T, q_recv, L)
                IS_EXIT = True
                break
            else:
                SB.add2que(q_recv, msg.decode("utf-8"))
                SB.updateRecv(T, q_recv, L)
        except socket.timeout:
            if IS_EXIT:
                break

    writer.close()
    reader.close()
    w.join()
    print('client is offline')


def add2que(q, e):
    if q.full():
        q.get()
        q.put(e)
    else:
        q.put(e)


if __name__ == '__main__':
    main()

