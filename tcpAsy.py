import asyncio
import socket


async def serveclient(s_client, n):
    s_client.send(b'hello')
    loop = asyncio.get_event_loop()
    data = await loop.sock_recv(s_client,1024)
    if data:
        print(f"client{n} send: {data}")
    s_client.send(b'bye')
    s_client.close()


async def linsten(s):
    loop = asyncio.get_event_loop()
    n = 0
    while True:
        s_client, addr_client = await loop.sock_accept(s)
        n = n + 1
        s_client.setblocking(False)
        loop.create_task(serveclient(s_client, n))


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 9999))
s.listen(5)
s.setblocking(False)
print('Asy server is working ...')

try:
    loop = asyncio.get_event_loop()
    loop.create_task(linsten(s))
    loop.run_forever()
except KeyboardInterrupt:
    for task in asyncio.Task.all_tasks():
        task.cancel()
finally:
    loop.run_until_complete(loop.shutdown_asyncgens())
    loop.close()
    s.close()
    print('server closed')
