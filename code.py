__author__ = 'Colby'
# execfile('code.py') to import into python console to use
# get_cords for gettings game button x and y positions

import time
import win32api, win32con

x_pad = 361
y_pad = 344

# import game button coordinates
class Cord:

    f_shrimp = (94, 851)
    f_rice = (222, 839)
    f_nori = (125, 972)
    f_roe = (236, 984)
    f_salmon = (90, 1110)
    f_unagi = (229, 1116)

def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0 ,0)
    print("Click")

def leftDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(.1)
    print("left down")

def leftUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0 ,0)
    time.sleep(.1)
    print("left release")

def mousePos(cord):
    win32api.SetCursorPos((x_pad + cord[0], y_pad + cord[1]))

def get_cords():
    x, y = win32api.GetCursorPos()
    x = x - x_pad
    y = y - y_pad
    print(x, y)

def startGame():
    # first play button
    mousePos((883, 524))
    leftClick()
    time.sleep(1)

    # second continue button
    mousePos((887, 971))
    leftClick()
    time.sleep(2)

    # third continue button
    mousePos((925, 1020))
    leftClick()
    time.sleep(2)

    # fourth skip button
    mousePos((1477, 1154))
    leftClick()
    time.sleep(2)

    # final continue button
    mousePos((906, 928))
    leftClick()
    time.sleep(2)

def main():
    pass

# # Python convention to check if script is top level (only executes if ran by itself)
# if __name__ == '__main__':
#     main()
