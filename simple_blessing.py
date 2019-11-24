from blessings import Terminal
from queue import Queue


'''
===online users===


===msg recv=======


===msg send=======


'''

def updateUsers(T, q_user):
    with T.location(0, 0):
        print(T.red('===online users==='))
        msg = ''
        for user in q_user.queue:
            msg += user + ', '
        print(T.red(msg))


def updateRecv(T, q_recv, L):
    with T.location(0, L):
        print(T.green('===msg recv======='))
        for msg in q_recv.queue:
            print(T.green(msg))


def updateSend(T, q_send, L):
    with T.location(0, 2*L):
        print(T.blue('===msg send======='))
        for msg in q_send.queue:
            print(T.blue(msg))


def add2que(q, e):
    if q.full():
        q.get()
        q.put(e)
    else:
        q.put(e)


def freshTer(T, q_user, q_recv, q_send, L):
    print(T.clear)
    for i in range(T.height-2):
        print('')
    updateUsers(T, q_user)
    updateRecv(T, q_recv, L)
    updateSend(T, q_send, L)


def main():
    T = Terminal()
    H = T.height
    L = H // 3
    promote = '>>>'

    q_user = Queue(L - 1)
    q_recv = Queue(L - 1)
    q_send = Queue(L - 2)


    freshTer(T, q_user, q_recv, q_send, L)

    while True:
        msg = input(promote)

        if msg == 'bye':
            print(T.clear)
            break
        elif len(msg) == 6:
            add2que(q_user, msg)
        else:
            add2que(q_send, msg)

        freshTer(T, q_user, q_recv, q_send, L)



if __name__ == '__main__':
    main()

