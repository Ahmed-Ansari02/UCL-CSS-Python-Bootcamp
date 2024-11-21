import time

print(f"current time is {time.time()}")
print("sleeping for 5 seconds")
time.sleep(5)
print("done sleeping")
print(f"current time is {time.time()}")
print(f"current time in local time zone is {time.ctime()}")
print(f"current time is {time.localtime()}")
print(f"current time in local timezone is {time.asctime(time.localtime())}")