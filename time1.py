import time

t = time.time()
for i in range(2):
    print(i)
    time.sleep(0.5)

print("The time for execting module", time.time() - t)

print(time.localtime())
print(time.asctime())

