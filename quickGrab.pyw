__author__ = 'Colby'

import ImageGrab
import os
import time

x_pad = 361
y_pad = 344

def screenGrab():
    box = (x_pad+1, y_pad+1, x_pad+1601, y_pad+1201)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')

def main():
    screenGrab()

# Python convention to check if script is top level (only executes if ran by itself)
if __name__ == '__main__':
    main()
