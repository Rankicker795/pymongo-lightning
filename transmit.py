import random
import socket
import time
from datetime import datetime, timezone
from functools import partial


def main(lat, lon, dt):
    return f"{lat}, {lon}, {dt}"


def send_mess(mess, sock, ip, pt):
    sock.sendto(mess.encode("utf-8"), (ip, pt))


UDP_IP = "127.0.0.1"
UDP_PORT = 50001
NUM_MSG = 100_000

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

mess_gen = (
    main(
        random.uniform(-90.0, 90.0),
        random.uniform(-180.0, 180.0),
        datetime.now(tz=timezone.utc),
    )
    for i in range(100_000)
)

partial_send = partial(send_mess, sock=s, ip=UDP_IP, pt=UDP_PORT)

count = 0

start_time = time.perf_counter()

for msg in mess_gen:
    if (count % 25) != 0:
        print("SENDING MSG!!!")
        partial_send(msg)
    else:
        print("SLEEPING!!!")
        time.sleep(0.1)
    count = count + 1

print(f"Took {time.perf_counter() - start_time} secs to transmit {NUM_MSG} messages")
