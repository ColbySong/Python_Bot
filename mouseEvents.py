__author__ = 'Colby'

import time
import win32api, win32con

x_pad = 361
y_pad = 344

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

def getCords():
    x, y = win32api.GetCursorPos()
    x = x - x_pad
    y = y - y_pad
    print(x, y)