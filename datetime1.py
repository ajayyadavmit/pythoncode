import time 

print(time.time())

print(time.localtime())
print(time.asctime())
t1 = time.time()

time.sleep(2)
print("the time vaue", time.time() - t1, "seconds")



import datetime

x = datetime.datetime.now()
print(x)
print(x.strftime("%M"))

y= datetime.datetime(2032,2,4)
print(y)

import datetime as dt 

print(dt.datetime.now())

y = dt.datetime(1222,2,22)
print(y)

x = dt.datetime.now()
print(x.strftime("%B"))
