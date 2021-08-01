import pyautogui, sys
from AppKit import NSScreen

print(NSScreen.mainScreen().frame())

hours = int(sys.argv[1])
mins = int(sys.argv[2])
hoursToSeconds = 0
minsToSeconds = 0

if(hours != 0):
    hoursToSeconds = hours * 60 * 60
else:
    hours = 0

if(mins != 0):
    minsToSeconds = mins * 60
else:
    mins = 0

totalTime = (hoursToSeconds + minsToSeconds)

print(str(hours) + " hours + " + str(mins) + " mins = " + str(totalTime) + " seconds")

for x in range(totalTime):
    if(x%2==0):
        pyautogui.moveTo(NSScreen.mainScreen().frame().size.width/2, NSScreen.mainScreen().frame().size.height/2, duration = 0.5)
        print("up")
    if(x%2!=0):
        pyautogui.moveTo((NSScreen.mainScreen().frame().size.width/2), (NSScreen.mainScreen().frame().size.height/2)-200, duration = 0.5)
        print("down")