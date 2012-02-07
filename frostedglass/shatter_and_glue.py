import random
import Image, ImageFont, ImageDraw
import rwparameters
import frost
import random

def show_breaks(pane, params):
    """
    Show red lines corresponding to where the message will be broken into tiles.
    """

    brokenpane = pane
    xmargin = params["xmargin"]
    ymargin = params["ymargin"]
    glasswidth = brokenpane.getbbox()[2] - (2 * xmargin)
    glassheight = brokenpane.getbbox()[3] - (2 * ymargin)
    shardwidth = glasswidth // params["shardswide"]
    shardheight = glassheight // params["shardstall"]
    
    vlines = [shardwidth * x + xmargin 
              for x in range(params["shardswide"] + 1)] # The x-coordinates
    hlines = [shardheight * y + ymargin 
              for y in range(params["shardstall"] + 1)] # The y-coordinates

    #print(vlines, hlines)
    draw = ImageDraw.Draw(brokenpane)
    # TODO fix this so the lines show up in red.
    for y in hlines:
        draw.line(((xmargin, y), (xmargin + glasswidth, y)), fill='rgb(255,0,0)')
    for x in vlines:
        draw.line(((x, ymargin), (x, ymargin + glassheight)), fill='rgb(255,0,0)')

    brokenpane.show()


def break_glass(pane, params):
    """
    Cut the image into tiles, then place the tiles, in order, into a list
    
    params is a dictionary of parameters from readparameters()
    """
    
    shardswide = params['shardswide']
    shardstall = params['shardstall']
    xmargin = params['xmargin']
    ymargin = params['ymargin']
    
    # bbox is the bounding tuple of the image (left, top, right, bottom)
    bbox = pane.getbbox()

    glass_left = xmargin
    glass_top = ymargin
    glass_right = bbox[2] - xmargin
    glass_bottom = bbox[3] - ymargin
    
    # This next is to make sure that the tiles (shards) evenly
    # partition the image (glass).
    while (glass_right - glass_left) % shardswide != 0:
        glass_right += 1
    while (glass_bottom - glass_top) % shardstall != 0:
        glass_bottom += 1
    shardwidth = (glass_right - glass_left)//shardswide
    shardheight = (glass_bottom - glass_top)//shardstall
    glasswidth = glass_right - glass_left
    glassheight = glass_bottom - glass_top

    print('shardwidth %d\nshardheight %d\nglasswidth %d\nglassheight %d') % (shardwidth, shardheight, glasswidth, glassheight) # Just testing things out here

    # Okay, now let's bust this thing.
    brokenglass = []
    for y in range(ymargin, ymargin + glassheight, shardheight):
        for x in range(xmargin, xmargin + glasswidth, shardwidth):
            shard = pane.crop((x, y, x + shardwidth, y + shardheight))
            brokenglass.append(shard)
    
    return brokenglass


def glue(dustpan, params):
    """
    Reconstruct the image so it can be read.

    dustpan - jumbled sequence of tiles
    params - a dictionary of parameters generated by readparameters()
 
    e.g. perm[0] == 5 --> first element in dustpan is the 6th element in the
    actual image
    """

    shardswide = params['shardswide']
    shardstall = params['shardstall']
    xmargin = params['xmargin']
    ymargin = params['ymargin']
    
    shard_dimensions = dustpan[0].getbbox()
    shardwidth = shard_dimensions[2]  # i.e. the right edge of the first element of dustpan
    shardheight = shard_dimensions[3]

    # Get the correct dimensions in order to reassemble the image
    glasswidth = shardwidth*shardswide
    # glassheight = shardheight*((len(dustpan)//shardsperline + 1) if len(dustpan) % shardsperline != 0 else len(dustpan)//shardsperline)
    glassheight = shardheight*shardstall

    panewidth = glasswidth + 2*xmargin
    paneheight = glassheight + 2*ymargin
    # gbbox = glass.getbbox()
    print('length of dustpan %d\nglasswidth %d\n glassheight %d\nshardbbox %s') % (len(dustpan), glasswidth, glassheight, shard_dimensions)

    # Create the backdrop against which all the tiles will be pasted
    gluedpane = Image.new('RGB', (panewidth, paneheight), color=(255, 255, 255))
    gluedpane = frost.frost(gluedpane)
    
    # Put the pieces back together
    dusty = iter(dustpan)
    glass = Image.new('RGB', (glasswidth, glassheight), color=(255, 255, 255))
    for y in range(0, glassheight, shardheight):
        for x in range(0, glasswidth, shardwidth):
            try:
                glass.paste(dusty.next(), (x, y))
            except StopIteration:
                glass.paste(dustpan[random.randint(0, len(dustpan) - 1)], (x, y))
    
    # Put the glued tiles (glass) against the backdrop (pane)
    gluedpane.paste(glass, (xmargin, ymargin))
    rwparameters.writeparameters(gluedpane, params)

    return gluedpane  # Nobody will notice :)

