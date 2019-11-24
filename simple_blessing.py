from blessings import Terminal
from queue import Queue


'''
===online users===


===msg recv=======


===msg send=======


'''

T = Terminal()
H = T.height
L = H//3

q_user = Queue(L-1)
q_recv = Queue(L-1)
q_send = Queue(L-2)
msg_user = ''



def updateUsers():
    with T.location(0, 0):
        print('===online users===')
        msg = ''
        for user in q_user.queue:
            msg += user + ', '
        print(msg)


def updateRecv():
    with T.location(0, L):
        print('===msg recv=======')
        for msg in q_recv.queue:
            print(msg)


def updateSend():
    with T.location(0, 2*L):
        print('===msg send=======')
        for msg in q_send.queue:
            print(msg)


def add2que(q, e):
    if q.full():
        q.get()
        q.put(e)
    else:
        q.put(e)


def freshTer():
    global T
    global H
    print(T.clear)
    for i in range(H-2):
        print('')
    updateUsers()
    updateRecv()
    updateSend()


freshTer()

while True:
    msg = input('>>>')

    if msg == 'bye':
        print(T.clear)
        break
    elif len(msg) == 6:
        add2que(q_user, msg)
    else:
        #add2que(q_recv, msg)
        add2que(q_send, msg)

    freshTer()





