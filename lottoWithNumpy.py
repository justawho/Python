import numpy as np
import time
import random

start1 = time.time()

rows         = 500
array        = np.random.randint(1,70,(rows,5),dtype=np.uint8)
sorted_array = np.sort(array,axis=1)

end1 = time.time()

print("miliseconds 1: {}".format((end1 - start1)*1000))


start2 = time.time()

count = 0
while( count < 500):

    draw = sorted(random.sample(range(1, 69), 5))
    count += 1

end2 = time.time()

print("miliseconds 2: {}".format((end2 - start2)*1000))
