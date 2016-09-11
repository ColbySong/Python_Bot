__author__ = 'Colby'

import ImageGrab
import ImageOps  # used for grayscaling
from numpy import *
import os
import time

x_pad = 361
y_pad = 344

# grabs the game screen, used for getting image coordinates
def screenGrab():
    box = (x_pad+1, y_pad+1, x_pad+1601, y_pad+1201)
    im = ImageGrab.grab(box)
    # im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')
    return im

# grab customer order images, used for determining sushi type
def grabOrderOne():
    box = (66,154,66+63,154+16)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print a
    im.save(os.getcwd() + '\\order_one__' + str(int(time.time())) + '.png', 'PNG')
    return a

def grabOrderTwo():
    box = (319,154,319+63,154+16)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print a
    im.save(os.getcwd() + '\\order_two__' + str(int(time.time())) + '.png', 'PNG')
    return a

def grabOrderThree():
    box = (571,154,571+63,154+16)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print a
    im.save(os.getcwd() + '\\order_three__' + str(int(time.time())) + '.png', 'PNG')
    return a

def grabOrderFour():
    box = (824,154,824+63,154+16)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print a
    im.save(os.getcwd() + '\\order_four__' + str(int(time.time())) + '.png', 'PNG')
    return a

def grabOrderFive():
    box = (1076,154,1076+63,154+16)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print a
    im.save(os.getcwd() + '\\order_five__' + str(int(time.time())) + '.png', 'PNG')
    return a

def grabOrderSix():
    box = (1329,154,1329+63,154+16)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print a
    im.save(os.getcwd() + '\\order_six__' + str(int(time.time())) + '.png', 'PNG')
    return a

def main():
    screenGrab()

# Python convention to check if script is top level (only executes if ran by itself)
if __name__ == '__main__':
    main()
