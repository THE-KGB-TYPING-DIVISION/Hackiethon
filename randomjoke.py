from flask import Flask
import time
import random

def countdown(t):
    while t:
        mins, secs = divmod(t,60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer,end = "\r")
        time.sleep(1)
        t -= 1
    print("end timer")
countdown(10)
print("debug")
numb = random.randint(1,5)
if numb == 1:
    print("Why did Steve fall off the tractor")
    print("because Steve was a strawberry")
elif numb == 2:
    print("My wife told me to stop acting like a flamingo")
    print("So I had to put my foot down")
elif numb == 3:
    print("Did you hear about the mathematician")
    print("He’ll stop at nothing to avoid them.")
elif numb == 4:
    print("Did you hear about the restaurant called Karma?")
    print("There is no menu, you get what you deserve")
elif numb == 5:
    print("Did you hear about the actor who fell through the floorboards?")
    print("He was probably just going through a stage.")
