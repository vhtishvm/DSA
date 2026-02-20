import numpy as np
import time

ls1 = [[1,2],
       [3,4]]
ls2 = [[5,6],
       [7,8]]

arr1 = np.array(ls1)
arr2 = np.array(ls2)
start = time.time()
arr3 = arr1@arr2
end = time.time()

print(f"Function executed in: {end-start}")
print(arr3)

''''This is almost 5 times faster that if we do matrix multiplication from scratch'''