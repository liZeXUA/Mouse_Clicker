from pynput.mouse import Button, Controller
import time

t = int(input("Wait times:"))
i = int(input("Times:"))
j = input("Interval time:")

time.sleep(t)

try:
    j = float(j)
except:
    raise ValueError("Please enter a positive integer!")


mouse = Controller()

for x in range(i+1):
    mouse.click(Button.left, i)
    time.sleep(j)

print("finished")
