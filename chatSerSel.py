import selectors
import socket
import threading

IS_EXIT = False


def serverwrite():
    while True:
        msg = input('speak like: user-msg\n')

        if IS_EXIT:
            print('writer thread closed')
            break

        pos = msg.find('-')
        if pos == -1 :
            print("wrong form, don't know which user to send")
        else:
            user = msg[0:pos]
            words = msg[pos+1:]
            if user in WRITERS.keys():
                WRITERS[user].send(words.encode('utf-8'))
            else:
                print(f'user {user} is offline')





ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.bind(('127.0.0.1', 9999))
ss.listen(5)
n = 0
print('Sel server is working ...')

sel = selectors.DefaultSelector()
sel.register(ss, selectors.EVENT_READ, data=(-1, -1))
USERS = set()
LOGUSERS = set()
WRITERS = dict()

writer = threading.Thread(target=serverwrite)


try:
    writer.start()
    while True:
        events = sel.select()
        for key, mask in events:
            User, type = key.data
            s = key.fileobj

            if type == -1:
                s_client, addr_client = s.accept()
                name = s_client.recv(512).decode('utf-8')

                if name in USERS:
                    print(f'user {name} begin to read')
                    if name in LOGUSERS:
                        s_client.send(f'{name} already login')
                        s_client.close()
                    else:
                        s_client.send('OK'.encode('utf8'))
                        # socket to write
                        WRITERS[name] = s_client
                        LOGUSERS.add(name)
                else:
                    print(f'user {name} begin to write')
                    s_client.send(f'hello: {name}'.encode('utf8'))
                    USERS.add(name)
                    # socket to recv
                    sel.register(s_client, selectors.EVENT_READ, data=(name, 0))

            elif type == 0:
                msg = s.recv(2048)
                if not msg or msg.decode('utf-8') == 'bye':
                    sel.unregister(s)
                    s.close()
                    print(f'{name} is logout')
                    USERS.remove(name)
                    LOGUSERS.remove(name)
                    WRITERS.pop(name)
                else:
                    print(f'{name} : {msg}')
except:
    IS_EXIT = True
    print('type any to exit')
    writer.join()
    print('Server closed')
finally:
    sel.close()
    ss.close()

