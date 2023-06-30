import numpy as np
import asyncio
import websockets
from multiprocessing import shared_memory
import time

try:
    position = shared_memory.SharedMemory(name = "attribute")
    droneposition = np.ndarray((3,), dtype = np.float64, buffer= position.buf)
except Exception:
    position2 = shared_memory.SharedMemory(create = True, size = 1024 ,name = "attri")
    droneposition = np.ndarray((3,), dtype = np.float64, buffer= position2.buf)


async def listen():
    url = "ws://127.0.0.1:7890"
    async with websockets.connect(url) as ws:
        while True:
            await ws.send(str(droneposition))
            msg = await ws.recv()
            print(msg)
            await asyncio.sleep(1)

asyncio.get_event_loop().run_until_complete(listen())
asyncio.get_event_loop().run_forever()