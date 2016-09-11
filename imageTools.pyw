__author__ = 'Colby'

import ImageGrab
import ImageOps  # used for grayscaling
from numpy import *
import os
import time

x_pad = 363
y_pad = 344

# grabs the game screen, used for getting image coordinates
def screenGrab():
    box = (x_pad+1, y_pad+1, x_pad+1601, y_pad+1201)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')
    return im

# grab customer order images, used for determining sushi type
def grabOrderOne():
    box = (x_pad+66,y_pad+154,x_pad+66+150,y_pad+154+30)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print a
    # im.save(os.getcwd() + '\\order_one__' + str(int(time.time())) + '.png', 'PNG')
    return a

def grabOrderTwo():
    box = (x_pad+319, y_pad+154, x_pad+319+150, y_pad+154+30)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print a
    # im.save(os.getcwd() + '\\order_two__' + str(int(time.time())) + '.png', 'PNG')
    return a

def grabOrderThree():
    box = (x_pad+571, y_pad+154, x_pad+571+150, y_pad+154+30)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print a
    # im.save(os.getcwd() + '\\order_three__' + str(int(time.time())) + '.png', 'PNG')
    return a

def grabOrderFour():
    box = (x_pad+824, y_pad+154, x_pad+824+150, y_pad+154+30)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print a
    # im.save(os.getcwd() + '\\order_four__' + str(int(time.time())) + '.png', 'PNG')
    return a

def grabOrderFive():
    box = (x_pad+1076, y_pad+154, x_pad+1076+150, y_pad+154+30)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print a
    # im.save(os.getcwd() + '\\order_five__' + str(int(time.time())) + '.png', 'PNG')
    return a

def grabOrderSix():
    box = (x_pad+1329, y_pad+154, x_pad+1329+150, y_pad+154+30)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print a
    # im.save(os.getcwd() + '\\order_six__' + str(int(time.time())) + '.png', 'PNG')
    return a

def getAllOrders():
    grabOrderOne()
    grabOrderTwo()
    grabOrderThree()
    grabOrderFour()
    grabOrderFive()
    grabOrderSix()

def main():
    screenGrab()

# Python convention to check if script is top level (only executes if ran by itself)
if __name__ == '__main__':
    main()
