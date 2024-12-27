#How to get time of a python program's Execution

import time#How long code takes to run
#time module it provides various time related functions
def timee():
    start_time = time.time()#returns the current time
    s = 0 #hold sum(1-n)
    for i in range(1,n+1):
        s = s + i

    end_time = time.time()#Return current time
    return s , end_time - start_time
n = 5
print(timee())