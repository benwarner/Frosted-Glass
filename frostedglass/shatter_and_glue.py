"""
Shatter is to permute the image


Basic steps:
    Create an image
    Fuzz the image, to prevent computerized recognition
    Permute or scramble the image

    [Send to someone else]

    Unpermute image, recognizable by human sight, but not by computer OCR

    image_creation: snapshot
    etch - write words onto the "glass" of the computer screen
    frost - process words to prevent computer recognition
    shatter_and_glue - scramble and unscramble image

    etchasketch - the driver that uses the other pieces
"""

import Image
import random
import ImageFont, ImageDraw

# seed = sys.argv[1]
X = 800
Y = 600

#messagefont = ImageFont.truetype("arial.ttf", 15)

#pane = Image.open("aoeuhtns.ppm")
#x, y = pane.size


# TODO get these "global" variables cleaned up
xmargin = 10
ymargin = 10
glasswidth = X - 2 * xmargin
glassheight = Y - 2 * ymargin

shardwidth = 15
shardheight = 15

def crack(pane):
    """
    Cut the image into tiles, then place the tiles, in order, into a list
    
    This is like how a cracked pane is still in place.
    """

    crackedglass = []
    for j in range(ymargin, glassheight, shardheight):
        for i in range(xmargin, glasswidth, shardwidth):
            shardoutline = (i, j, i + shardwidth, j + shardheight)
            shard = pane.crop(shardoutline)
            crackedglass.append(shard)
    
    return crackedglass

def genperm(crackedglass, seed):
    random.seed(seed)
    perm = range(len(crackedglass))
    random.shuffle(perm) # This shuffles the list in place.
    # Figure out later how to do this via permutation numbering.
    
    return perm

def shatter(crackedglass, perm):
    """
    Permute ordered list of tiles into random sequence

    The dustpan holds the random collection of tiles.
    """
    dustpan = []
    for i in perm:
        dustpan.append(crackedglass[i])

    return dustpan

def the_real_shatter(pane, key):
    """
    Scramble the image according to key

    By the way, key is also key to unscramble the image

    returns dustpan - scrambled list of images
    """
    
    # cracky is a list of images
    cracky = crack(pane)
    # frizzy is a permuted list of integers between 0 and number of tiles
    frizzy = genperm(cracky, key)
    # dust is a scrambled list of images
    dust = shatter(cracky, frizzy)
    return dust


# TODO clean up X and Y
def glue(dustpan, perm, x=X, y=Y):
    """
    Reconstruct the image so it can be read.

    dustpan - jumbled sequence of tiles
    perm - list of indices to tiled list, in random order 
        
    e.g. perm[0] == 5 --> first element in dustpan is the 6th element in the
    actual image
    """
    # Rearrange the shards so that they can be glued in sequence.
    orderedtaggedshards = sorted(zip(perm, dustpan))
    orderedshards = []
    for i in orderedtaggedshards:
        orderedshards.append(i[1]) # Is there an easier way to do this?
    
    gluedpane = Image.new('RGB', (x, y), color = (255, 255, 255))
    nextshard = 0
    for j in range(ymargin, glassheight, shardheight):
        for i in range(xmargin, glasswidth, shardwidth):
            shardoutline = (i, j, i + shardwidth, j + shardheight)
            gluedpane.paste(orderedshards[nextshard], shardoutline)
            nextshard += 1 # Do this with an 'iterable' instead?

    return gluedpane

def the_real_glue(dustpan, key):
    """
    Unpermutes list of images, "glues" into singal image according to key

    """
    perm = genperm(dustpan, key)
    return glue(dustpan, perm)


