
import time as t

# print(dir(time))

def start_time():
    time = 60 * 60
    while time >=  0:
        # time = int(input("set Time(mins): ")) * 60
        minutes = time // 60 
        seconds = time % 60
        minutes = "0"+str(minutes) if minutes < 10 else minutes
        seconds = "0"+str(seconds) if seconds < 10 else seconds

        timers = f"{minutes} : {seconds}"
        print(timers)
        t.sleep(1)
        time -= 1
if __name__ == "__main__":
    start_time()