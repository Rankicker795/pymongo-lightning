# pymongo-lightning
Software to test the capabilities of the Asynchronous PyMongo Engine for a high velocity dataset.

### Scripts

*transmit.py* - Module to simulate sending 100,000 lightning strikes events over UDP to be processed by the receiver.

*receive.py* - Module to decode the incoming byte string from the UDP socket, transform it into a dict, and insert the dict into the lightning.strikes collection using PyMongo and asyncio.

### Running the software

```shell

python receive.py <mongodb.uri> <queue_size> &
python transmit

```
