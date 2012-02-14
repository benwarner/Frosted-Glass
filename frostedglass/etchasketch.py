"""
Do all the etching, frosting, shattering, glueing, and everything else.

This is the file you want to use to get anything practical done.
"""

from rwparameters import *
from etch import *
from shatter_and_glue import *
from frost import *

def readmessagefile(messagefile):
    """
    Takes in a text file and returns a string.
    """
    openfile = open(messagefile)
    message = openfile.read()
    
    return message


def shatter(pane, key, params=None):
    """
    Scramble the image according to key

    By the way, key is also key to unscramble the image

    returns uh_oh - an image with rearranged tiles
    """
    
    if not params:
        params = makeparameters()

    # shards is a list of images
    shards = break_glass(pane, params)
    
    # dustpan is a scrambled list of images
    dustpan = scramble(shards, key)
    
    # uh_oh is the permuted list of tiles from dustpan reassembled
    # back into a single image.
    uh_oh = glue(dustpan, params)
    
    writeparameters(uh_oh, params)

    return uh_oh


def restore(pane, key):
    """
    Take an image with scrambled tiles and restore it to readable form

    Much like shatter but using the unscramble rather than scramble method
    """
    
    params = readparameters(pane)
    shards = break_glass(pane, params)
    mosaic = unscramble(shards, key)
    good_as_new = glue(mosaic, params)

    return good_as_new


def main():
    message_file = "thesecret.txt"
    msg = readmessagefile(message_file)
    etched_image = etch(msg, font_size=30, xmargin=20, ymargin=20)
    etched_image.show()
    frosted_image = frost(etched_image, frostyness=.3)
    scrambled_list_of_images = the_real_shatter(frosted_image, key=9999)
    # gluing with the wrong key, for illustration purposes
    raw_input("The wrong way> ")
    badasnew = the_real_glue(scrambled_list_of_images, key=0)
    badasnew.show()
    raw_input("The right way (with the proper key)> ")
    goodasnew = the_real_glue(scrambled_list_of_images, key=9999)
    goodasnew.show()


if "__main__" == __name__:
    main()
