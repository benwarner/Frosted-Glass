"""
Process image of text so that it is unrecognizable by a computer algorithm

Analogy: text is written on glass, and then we "frost" the image on the glass.
"""

import Image
import random

def convert_point(pt):
    pt = pt ^ (random.randint(0,1)*255)

def convert_list(_list, frostyness):
    """
    XOR the image (stored as 0s and 1s) with a random sequence of 0s and 1s.

    The frostyness parameter should be between 0 and 1. 
    frostyness=0 will result in no frosting of the image, while frostyness=1
    will result in purely random noise.
    """
    noiselevel = frostyness / 2
    for x in range(len(_list)):
        _list[x] = _list[x] ^ int(1 if random.random() < noiselevel else 0)

def convert_to_01(data):
    return [1 if 0 < x else 0 for x in data]

def convert_to_255(data):
    return [255 if 0 < x else 0 for x in data]

def frost(pane, frostyness=.35):
    """
    Speckle the image with black and white pixels in order to "fuzz" edges.

    frostyness should be between 0 and 1.
    """
    
    bwimg = pane.convert('1')
    d = bwimg.getdata()
    bindata = convert_to_01(d)
    convert_list(bindata, frostyness)
    data255 = convert_to_255(bindata)
    bwimg.putdata(data255)
    
    return bwimg

