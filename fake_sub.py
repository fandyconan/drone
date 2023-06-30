import numpy as np
import asyncio
import websockets
from multiprocessing import shared_memory
import time

pos = np.array(
    [[100.11,9.55,51.12],
     [103.12,12.48,48.76],
     [102.48,11.75,49.33],
     [100.99,13.01,52.14],
     [100.58,11.87,51.44],
     [102.32,13.44,48.92],
     [103.09,12.73,49.69],
     [102.29,11.49,52.22],
     [103.12,12.48,48.76],
     [102.48,11.75,49.33]])
try:
    position = shared_memory.SharedMemory(name = "attri")
    droneposition = np.ndarray((3,), dtype = np.float64, buffer= position.buf)
except Exception:
    position2 = shared_memory.SharedMemory(create = True, size = 1024 ,name = "attribute")
    droneposition = np.ndarray((3,), dtype = np.float64, buffer= position2.buf)


while True:
    for row in pos:
        droneposition[:] = row[:] 
        print(droneposition)
        time.sleep(0.5)
    


# except Exception:
#     position2 = shared_memory.SharedMemory(name = "attribute")
#     droneposition = np.ndarray((3,), dtype= np.float64, buffer= position.buf)





   