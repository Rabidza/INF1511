from time import time, ctime

prev_time = ""
while True:
    curr_time = ctime(time())
    if prev_time != curr_time:
        print("The time is:", ctime(time()))
        prev_time = curr_time
