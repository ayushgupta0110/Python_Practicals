import random
import time
n=10000
lst=list(range(n))
random.shuffle(lst)
s=set(lst)
starttime=time.time()
for i in range(n):
    i in s
endtime=time.time()
runtime=int((endtime-starttime)*1000)
print("to test if ",n,"elements in set The run time is: ",runtime,"ms")


starttime=time.time()
for i in range(n):
    i in lst
endtime=time.time()
runtime=int((endtime-starttime)*1000)
print("to test if ",n,"elements in list The run time is: ",runtime,"ms")

starttime=time.time()
for i in range(n):
    s.remove(i)
endtime=time.time()
runtime=int((endtime-starttime)*1000)
print("to test if ",n,"elements in set The run time to remove all is: ",runtime,"ms")


starttime=time.time()
for i in range(n):
    lst.remove(i)
endtime=time.time()
runtime=int((endtime-starttime)*1000)
print("to test if ",n,"elements in list The run time to remove all is: ",runtime,"ms")
