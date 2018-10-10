import asyncio


async def tcp_echo_client(message, loop):
    reader, writer = await asyncio.open_connection("127.0.0.1", 10001, loop=loop)

    print(f'send {message}')
    writer.write(message.encode())
    writer.close()


loop = asyncio.get_event_loop()

message1 = 'hello world'
message2 = 'goodbye world'

loop.run_until_complete(tcp_echo_client(message1, loop))
loop.run_until_complete(tcp_echo_client(message2, loop))
