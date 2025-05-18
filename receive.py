import asyncio
import socket
import sys

from pymongo import AsyncMongoClient

UDP_IP = "127.0.0.1"
UDP_PORT = 50001

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))


uri = sys.argv[1]
queue_size = int(sys.argv[2])


async def insert_doc():
    client = AsyncMongoClient(uri, maxPoolSize=None)

    db = client["lightning"]
    coll = db["strike"]
    insert_queue = []

    while True:
        data, addr = sock.recvfrom(1024)
        mess = (data.decode("utf-8")).split(",")
        mess_dict = {
            "lat": mess[0],
            "lon": mess[1],
            "date": mess[2],
        }
        if len(insert_queue) <= queue_size:
            insert_queue.append(mess_dict)
        else:
            await coll.insert_many(insert_queue)
            insert_queue = []


loop = asyncio.new_event_loop()
try:
    loop.run_until_complete(insert_doc())
except KeyboardInterrupt:
    print("Program terminated!!!")
