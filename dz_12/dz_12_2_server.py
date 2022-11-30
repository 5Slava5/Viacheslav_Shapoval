"""Сервер для приймання двох чисел та проведення з ними арифметичних дій з
використанням asincio"""
import socket
import asyncio

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 55000))
sock.listen(10)
print('Server is running, please, press ctrl+c to stop')
while True:
    conn, addr = sock.accept()
    print('connected:', addr)
    data = conn.recv(1024)
    num_1 = int((data.decode()))
    conn.send(bytes('Next please', encoding='UTF-8'))
    data = conn.recv(1024)
    num_2 = int((data.decode()))


    async def first(x: int, y: int):
        res_1 = x + y
        print(f'1 result of {x} + {y} = {res_1}')
        await asyncio.sleep(0)
        res_2 = x - y
        print(f'2 result of {x} - {y} = {res_2}')


    async def second(x: int, y: int):
        res_3 = x * y
        print(f'3 result of {x} * {y} = {res_3}')
        await asyncio.sleep(0)
        res_4 = x / y
        print(f'4 result of {x} / {y} = {res_4}')


    loop = asyncio.get_event_loop()
    tasks = [loop.create_task(first(num_1, num_2)), loop.create_task(second(num_1, num_2))]
    wait_tasks = asyncio.wait(tasks)
    loop.run_until_complete(wait_tasks)
    loop.close()
conn.close()
