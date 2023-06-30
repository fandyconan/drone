import numpy as np
import time

A = np.array([[100.11,9.55,51.12],
     [103.12,12.48,48.76],
     [102.48,11.75,49.33],
     [100.99,13.01,52.14],
     [100.58,11.87,51.44],
     [102.32,13.44,48.92],
     [103.09,12.73,49.69],
     [102.29,11.49,52.22]])
for row in A:
    print(row)
    time.sleep(5)


count = 1
for i in range(A.shape[0]):
    for j in range(A.shape[1]):
        for k in range(A.shape[2]):
            A[i, j, k] = count
            count += 1


print(A)