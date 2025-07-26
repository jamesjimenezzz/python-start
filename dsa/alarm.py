import datetime
import time


def set_alarm(alarm_time):
   
    is_running =  True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)

        if alarm_time == current_time:
            is_running = False

        time.sleep(1)



if __name__ == "__main__":
    alarm_time = input("What time do you want to alarm? HH:MM:SS: ")
    set_alarm(alarm_time)