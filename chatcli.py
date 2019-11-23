import socket
import threading


IS_EXIT = False


def online(writer, reader, addr, port, user):
    writer.connect((addr, port))
    writer.send(user.encode('utf-8'))

    data = writer.recv(128)
    print(data.decode('utf-8'))
    if data.decode('utf-8')[0:5] == 'hello':

        reader.connect((addr, port))
        reader.send(user.encode('utf-8'))
        data = reader.recv(128)
        if data.decode('utf-8') == 'OK' :
            print(f'{user} is online, type "bye" to offline')


def write(writer):
    global IS_EXIT
    while True:
        msg = input('msg>')
        if IS_EXIT:
            break

        writer.send(msg.encode('utf-8'))

        if msg == 'bye':
            IS_EXIT = True
            break


def main():
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
                print('server seems closed, type any to exit')
                IS_EXIT = True
                break
            else:
                print(f'\n server said: {msg.decode("utf-8")}')
        except socket.timeout:
            if IS_EXIT:
                break

    writer.close()
    reader.close()
    w.join()
    print('client if offline')


if __name__ == '__main__':
    main()

