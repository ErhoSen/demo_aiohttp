import asyncio
import random


async def send_message_client(message, loop):
    reader, writer = await asyncio.open_connection("127.0.0.1", 10001, loop=loop)

    print(f'send {message}')
    writer.write(message.encode())
    writer.close()


loop = asyncio.get_event_loop()

messages = ['hello world', 'goodbye world', 'hello goodbye', 'goodbye hello'] * 100

task_list = [loop.create_task(send_message_client(message, loop)) for message in messages]

loop.run_until_complete(asyncio.wait(task_list))

loop.run_until_complete(loop.create_task(send_message_client('message1', loop)))

loop.run_until_complete(asyncio.gather(
    send_message_client('message2', loop),
    send_message_client('message3', loop),
    send_message_client('message4', loop),
))
