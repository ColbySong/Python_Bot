__author__ = 'Colby'
# execfile('game.py') to import into python console to use
# get_cords for gettings game button x and y positions
from gameCoordinates import *
from mouseEvents import *
from imageTools import *

"""
Recipes:
onigiri: 2 rice, 1 nori
caliroll: 1 rice, 1 nori, 1 roe
gunkan: 1 roce, 1 nori, 2 roe
"""
# starting ingredient numbers
foodStock = {
    'rice': 10,
    'nori': 10,
    'roe': 10
}

# sushi order grayscale sum values
sushiValue = {
    7577: 'gunkan',
    9762: 'onigiri',
    13109: 'caliroll'
}

# blank seats values
blankSeats = {
    'seatOne': 15727,
    'seatTwo': 18607,
    'seatThree': 23474,
    'seatFour': 23658,
    'seatFive': 20130,
    'seatSix': 17072
}
####################################
def foldMat():
    mousePos((557, 839))
    leftClick()
    time.sleep(0.5)
####################################
def makeFood(food):
    if food == 'caliroll':
        print("making calirol")
        foodStock['rice'] -= 1;
        foodStock['nori'] -= 1;
        foodStock['roe'] -= 1;
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
        foodStock['rice'] -= 2
        foodStock['nori'] -= 1
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
        foodStock['rice'] -= 1
        foodStock['nori'] -= 1
        foodStock['roe'] -= 2
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
###############################################################
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

################################################################
def buyFood(food):
    if food == 'rice':
        mousePos(Cord.phone)
        time.sleep(.5)
        leftClick()
        mousePos(Cord.menu_rice)
        time.sleep(0.5)
        leftClick()
        im = screenGrab()
        time.sleep(0.5)
        if im.getpixel(Cord.buy_rice) != (127, 127, 127):
            print('rice is AVAILABLE')
            mousePos(Cord.buy_rice)
            time.sleep(.5)
            leftClick()
            mousePos(Cord.delivery_norm)
            print('BUYING RICE')
            foodStock['rice'] += 10
            time.sleep(.5)
            leftClick()
            time.sleep(3)
        else:
            print('rice is NOT AVAILABLE')
            mousePos(Cord.t_exit)
            leftClick()
            time.sleep(2)
            buyFood(food)

    if food == 'nori':
        mousePos(Cord.phone)
        time.sleep(.5)
        leftClick()
        mousePos(Cord.menu_toppings)
        time.sleep(0.5)
        leftClick()
        im = screenGrab()
        time.sleep(0.5)
        if im.getpixel(Cord.t_nori) != (33, 30, 11):
            print('nori is AVAILABLE')
            mousePos(Cord.t_nori)
            time.sleep(.5)
            leftClick()
            mousePos(Cord.delivery_norm)
            foodStock['nori'] += 10
            time.sleep(.5)
            leftClick()
            time.sleep(3)
        else:
            print('nori is NOT AVAILABLE')
            mousePos(Cord.t_exit)
            leftClick()
            time.sleep(2)
            buyFood(food)

    if food == 'roe':
        mousePos(Cord.phone)
        time.sleep(.5)
        leftClick()
        mousePos(Cord.menu_toppings)
        time.sleep(0.5)
        leftClick()
        im = screenGrab()
        time.sleep(0.5)
        if im.getpixel(Cord.t_roe) != (109, 123, 127):
            print('roe is AVAILABLE')
            mousePos(Cord.t_roe)
            time.sleep(.5)
            leftClick()
            mousePos(Cord.delivery_norm)
            foodStock['roe'] += 10
            time.sleep(.5)
            leftClick()
            time.sleep(3)
        else:
            print('roe is NOT AVAILABLE')
            mousePos(Cord.t_exit)
            leftClick()
            time.sleep(2)
            buyFood(food)
####################################################################
def checkFood():
    for i, j in foodStock.items():
        if j <= 4:
            print('%s is running low, please order' % i)
            buyFood(i)
####################################################################
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

def playGame():
    checkFood()
    orderOne = grabOrderOne() # this is a grayscale sum value
    if orderOne != blankSeats['seatOne']:
        if sushiValue.has_key(orderOne):
            sushiOrder = sushiValue[orderOne]
            print('Table One is ordering %s' % sushiOrder)
            makeFood(sushiOrder)
        else:
            print('Sushi order not found')
    else:
        print('No one is at Table One')

    clearTables()
    checkFood()
    orderTwo = grabOrderTwo() # this is a grayscale sum value
    if orderTwo != blankSeats['seatTwo']:
        if sushiValue.has_key(orderTwo):
            sushiOrder = sushiValue[orderTwo]
            print('Table Two is ordering %s' % sushiOrder)
            makeFood(sushiOrder)
        else:
            print('Sushi order not found')
    else:
        print('No one is at Table Two')

    clearTables()
    checkFood()
    orderThree = grabOrderOne() # this is a grayscale sum value
    if orderThree != blankSeats['seatThree']:
        if sushiValue.has_key(orderThree):
            sushiOrder = sushiValue[orderThree]
            print('Table Three is ordering %s' % sushiOrder)
            makeFood(sushiOrder)
        else:
            print('Sushi order not found')
    else:
        print('No one is at Table Three')

    clearTables()
    checkFood()
    orderFour = grabOrderFour() # this is a grayscale sum value
    if orderFour != blankSeats['seatFour']:
        if sushiValue.has_key(orderFour):
            sushiOrder = sushiValue[orderFour]
            print('Table Four is ordering %s' % sushiOrder)
            makeFood(sushiOrder)
        else:
            print('Sushi order not found')
    else:
        print('No one is at Table Four')

    clearTables()
    checkFood()
    orderFive = grabOrderFive() # this is a grayscale sum value
    if orderFive != blankSeats['seatFive']:
        if sushiValue.has_key(orderFive):
            sushiOrder = sushiValue[orderFive]
            print('Table Five is ordering %s' % sushiOrder)
            makeFood(sushiOrder)
        else:
            print('Sushi order not found')
    else:
        print('No one is at Table Five')

    clearTables()
    checkFood()
    orderSix = grabOrderSix() # this is a grayscale sum value
    if orderSix != blankSeats['seatSix']:
        if sushiValue.has_key(orderSix):
            sushiOrder = sushiValue[orderSix]
            print('Table Five is ordering %s' % sushiOrder)
            makeFood(sushiOrder)
        else:
            print('Sushi order not found')
    else:
        print('No one is at Table Six')

    clearTables()

def main():
    startGame()
    while True:
        playGame()

# Python convention to check if script is top level (only executes if ran by itself)
if __name__ == '__main__':
   main()
