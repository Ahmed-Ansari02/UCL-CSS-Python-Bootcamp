import time

print(f"current time is {time.time()}")
print("sleeping for 5 seconds")
time.sleep(2)
print("done sleeping")
print(f"current time is {time.time()}")
print(f"current time is {time.ctime()}")
print(f"current time is {time.localtime()}")
print(f"current time is {time.asctime(time.localtime())}")