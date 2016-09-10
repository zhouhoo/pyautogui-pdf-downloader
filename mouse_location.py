import pyautogui
import time
# print 'Press Ctrl-C to quit.'
# 获取鼠标坐标
try:
    while True:
 # TODO: Get and print the mouse coordinates.
        x,y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr)
except KeyboardInterrupt:
    print ('\nDone.')
