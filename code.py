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

    phone = (1433, 957)
    menu_toppings = (1361, 678)

    t_shrimp = (1238, 570)
    t_nori = (1237, 707)
    t_roe = (1466, 706)
    t_salmon = (1252, 854)
    t_unagi = (1448, 579)
    t_exit = (1462, 842)

    menu_rice = (1388, 737)
    buy_rice = (1379, 734)

    delivary_norm = (1243, 743)

"""
Recipes:
onigiri: 2 rice, 1 nori
caliroll: 1 rice, 1 nori, 1 roe
gunkan: 1 roce, 1 nori, 2 roe
"""
def foldMat():
    mousePos((557, 839))
    leftClick()
    time.sleep(0.5)

def makeFood(food):
    if food == 'caliroll':
        print("making caliroll")
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(0.5)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(0.5)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(0.5)
        foldMat()
        time.sleep(2)

    elif food == 'onigiri':
        print("making onigiri")
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(0.5)
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(0.5)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(0.5)
        foldMat()
        time.sleep(2)

    elif food == 'gunkan':
        print("making gunkan")
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(0.5)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(0.5)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(0.5)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(0.5)
        foldMat()
        time.sleep(2)

def clearTables():
    mousePos((204, 500))
    leftClick()

    mousePos((458, 516))
    leftClick()

    mousePos((710, 519))
    leftClick()

    mousePos((968, 518))
    leftClick()

    mousePos((1209, 528))
    leftClick()

    mousePos((1475, 527))
    leftClick()
    time.sleep(2)

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
