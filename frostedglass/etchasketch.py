"""
Do all the etching, frosting, shattering, glueing, and everything else.

This is the file you want to use to get anything practical done.
"""

from etch import etch
from frost import frost
from shatter_and_glue import the_real_shatter, the_real_glue

def readmessagefile(messagefile):
    """
    Takes in a text file and returns a string.
    """
    openfile = open(messagefile)
    message = openfile.read()
    
    return message

def main():
    message_file = "thesecret.txt"
    testing_key = 9999
    msg = readmessagefile(message_file)
    etched_image = etch(msg)
    etched_image.show()
    frosted_image = frost(etched_image, frostyness=2.2)
    scrambled_list_of_images = the_real_shatter(frosted_image, key=testing_key)
    # gluing with the wrong key, for illustration purposes
    raw_input("The wrong way> ")
    badasnew = the_real_glue(scrambled_list_of_images, key=0)
    badasnew.show()
    raw_input("The right way (with the proper key)> ")
    goodasnew = the_real_glue(scrambled_list_of_images, key=testing_key)
    goodasnew.show()


if "__main__" == __name__:
    main()
