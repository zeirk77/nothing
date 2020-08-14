from NO_Q import *
import pyautogui
import time


print(str(1))
time.sleep(1)
print(str(2))
time.sleep(1)
print(str(3))
time.sleep(1)
print('~~~~~ S T A R T ~~~~~')
f = open('texter.txt', 'r')
for line in f:
    pyautogui.typewrite(line)