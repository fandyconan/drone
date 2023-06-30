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




while True:
    print(droneposition)
    time.sleep(2)
   