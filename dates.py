
import datetime

current_time = datetime.datetime.now()
target_time =  datetime.datetime(2030, 1, 2 ,12, 30, 1)

if current_time < target_time:
    print("The target time has been passed.")
else:
    print("The target time is not been passed.")