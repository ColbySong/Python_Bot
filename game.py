__author__ = 'Colby'
# execfile('game.py') to import into python console to use
# get_cords for gettings game button x and y positions

import time
import win32api
import gameCoordinates
import mouseEvents

x_pad = 361
y_pad = 344

"""
Recipes:
onigiri: 2 rice, 1 nori
caliroll: 1 rice, 1 nori, 1 roe
gunkan: 1 roce, 1 nori, 2 roe
"""
def foldMat():
    mouseEvents.mousePos((557, 839))
    mouseEvents.leftClick()
    time.sleep(0.5)

def makeFood(food):
    if food == 'caliroll':
        print("making calirol")
        mouseEvents.mousePos(gameCoordinates.Cord.f_rice)
        mouseEvents.leftClick()
        time.sleep(0.5)
        mouseEvents.mousePos(gameCoordinates.Cord.f_nori)
        mouseEvents.leftClick()
        time.sleep(0.5)
        mouseEvents.mousePos(gameCoordinates.Cord.f_roe)
        mouseEvents.leftClick()
        time.sleep(0.5)
        foldMat()
        time.sleep(2)

    elif food == 'onigiri':
        print("making onigiri")
        mouseEvents.mousePos(gameCoordinates.Cord.f_rice)
        mouseEvents.leftClick()
        time.sleep(0.5)
        mouseEvents.mousePos(gameCoordinates.Cord.f_rice)
        mouseEvents.leftClick()
        time.sleep(0.5)
        mouseEvents.mousePos(gameCoordinates.Cord.f_nori)
        mouseEvents.leftClick()
        time.sleep(0.5)
        foldMat()
        time.sleep(2)

    elif food == 'gunkan':
        print("making gunkan")
        mouseEvents.mousePos(gameCoordinates.Cord.f_rice)
        mouseEvents.leftClick()
        time.sleep(0.5)
        mouseEvents.mousePos(gameCoordinates.Cord.f_nori)
        mouseEvents.leftClick()
        time.sleep(0.5)
        mouseEvents.mousePos(gameCoordinates.Cord.f_roe)
        mouseEvents.leftClick()
        time.sleep(0.5)
        mouseEvents.mousePos(gameCoordinates.Cord.f_roe)
        mouseEvents.leftClick()
        time.sleep(0.5)
        foldMat()
        time.sleep(2)

def clearTables():
    mouseEvents.mousePos((204, 500))
    mouseEvents.leftClick()

    mouseEvents.mousePos((458, 516))
    mouseEvents.leftClick()

    mouseEvents.mousePos((710, 519))
    mouseEvents.leftClick()

    mouseEvents.mousePos((968, 518))
    mouseEvents.leftClick()

    mouseEvents.mousePos((1209, 528))
    mouseEvents.leftClick()

    mouseEvents.mousePos((1475, 527))
    mouseEvents.leftClick()
    time.sleep(2)

def getCords():
    x, y = win32api.GetCursorPos()
    x = x - x_pad
    y = y - y_pad
    print(x, y)

def startGame():
    # first play button
    mouseEvents.mousePos((883, 524))
    mouseEvents.leftClick()
    time.sleep(1)

    # second continue button
    mouseEvents.mousePos((887, 971))
    mouseEvents.leftClick()
    time.sleep(2)

    # third continue button
    mouseEvents.mousePos((925, 1020))
    mouseEvents.leftClick()
    time.sleep(2)

    # fourth skip button
    mouseEvents.mousePos((1477, 1154))
    mouseEvents.leftClick()
    time.sleep(2)

    # final continue button
    mouseEvents.mousePos((906, 928))
    mouseEvents.leftClick()
    time.sleep(2)

def main():
    pass

# # Python convention to check if script is top level (only executes if ran by itself)
# if __name__ == '__main__':
#     main()
