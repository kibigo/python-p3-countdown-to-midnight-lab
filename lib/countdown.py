# your code goes here!
import time

x=5
def countdown(x):
    while x >0:
        print(f"{x} SECOND(S)!")
        if x == 1:
            print("HAPPY NEW YEAR!")
        x -=1

countdown(x)

def countdown_with_sleep(x):
    while x > 0:
        print(f"{x} SECOND(S)!")
        time.sleep(1)
        if x == 1:
            print("HAPPY NEW YEAR!")
        x -=1
countdown_with_sleep(x)