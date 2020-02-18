import asyncio
import socket
import time


#Wait function
async def sleep_func():
    await asyncio.sleep(10)

#Print "Hello world" function
async def print_hello(loop):
    i = 0
    while True:
        print("Hello world!")
        if i > 5000:
            loop.stop()
            break
        i += 1
        time.sleep(5)
        await sleep_func()

#Get data, print and wait
async def return_data(conn, loop):
    end_time = loop.time() + 60.0
    while True:
        data = conn.recv(1024)
        if not data:
            loop.stop()
            break
        else:
            print(data)
        if (loop.time() + 1.0) >= end_time:
            loop.stop()
            break
        await sleep_func()

if __name__ == "__main__":

    sock = socket.socket()
    sock.bind(('', 9092))
    sock.listen(1)
    conn, addr = sock.accept()

    print('connected:', addr)
    loop = asyncio.get_event_loop()

    asyncio.ensure_future(return_data(conn, loop))
    asyncio.ensure_future(print_hello(loop))

    loop.run_forever()
