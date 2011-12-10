import Image
import random

# seed = sys.argv[1]
seed = 9999

pane = Image.open("aoeuhtns.ppm")
x, y = pane.size

xmargin = 10
ymargin = 10
glasswidth = x - 2 * xmargin
glassheight = y - 2 * ymargin

shardwidth = 15
shardheight = 15

def crack(pane):
    """
    Cut the image into tiles, place tiles in order into list
    
    Same way that a cracked pane is still in place.
    """

    crackedglass = []
    for j in range(ymargin, glassheight, shardheight):
        for i in range(xmargin, glasswidth, shardwidth):
            shardoutline = (i, j, i + shardwidth, j + shardheight)
            shard = pane.crop(shardoutline)
            crackedglass.append(shard)
    
    return crackedglass

def genperm(crackedglass):
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

def glue(dustpan, perm):
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
    
    gluedpane = pane # Fix this later
    nextshard = 0
    for j in range(ymargin, glassheight, shardheight):
        for i in range(xmargin, glasswidth, shardwidth):
            shardoutline = (i, j, i + shardwidth, j + shardheight)
            gluedpane.paste(orderedshards[nextshard],shardoutline)
            nextshard += 1 # Do this with an 'iterable' instead?

    return gluedpane

pane.show()
cracky = crack(pane)
frizzy = genperm(cracky)
dusty = shatter(cracky, frizzy)
goodasnew = glue(dusty, frizzy)
raw_input("> ")
goodasnew.show()
goodasnew = glue(dusty, range(len(cracky)))
raw_input("> ")
goodasnew.show()
