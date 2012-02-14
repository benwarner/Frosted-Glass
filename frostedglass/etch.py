"""
Transfer a string of text onto an image

Analogy: etching a message on a piece of glass
"""

import Image
import ImageFont, ImageDraw
from random import randint

def crop_to_text(glass):
    """
    Reduce the left, top, bottom, and right until you bump into black text.
    """
    
    (left, top, right, bottom) = glass.getbbox()

    # Find the left border. 
    try:
        for j in range(right):
            for i in range(bottom):
                if glass.getpixel((j, i)) != (255, 255, 255):
                    newleft = j - 1
                    raise StopIteration()
    except StopIteration:
        pass

    # Find the top border.
    try:
        for j in range(bottom):
            for i in range(right):
                if glass.getpixel((i, j)) != (255, 255, 255):
                    newtop = j - 1
                    raise StopIteration()
    except StopIteration:
        pass
    
    # Find the right border.
    try:
        for j in range(right)[::-1]:
            for i in range(bottom):
                if glass.getpixel((j, i)) != (255, 255, 255):
                    newright = j + 1
                    raise StopIteration()
    except StopIteration:
        pass
    
    # Find the bottom border.
    try:
        for j in range(bottom)[::-1]:
            for i in range(right):
                if glass.getpixel((i, j)) != (255, 255, 255):
                    newbottom = j + 1
                    raise StopIteration()
    except StopIteration:
        pass
    
    # Make the new box by which to crop.
    cropbox = (newleft, newtop, newright, newbottom)
    glass = glass.crop(cropbox)

    return glass

def fill_remaining(pane, message, boxwidth, boxheight,
                   randxoffset, randyoffset, font_size,
                   xmargin, ymargin, widthremaining, x, y, 
                   font="/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf"):
    """
    Fill up the remainder of a line with garbage
    """
    
    draw = ImageDraw.Draw(pane)
    fnt = ImageFont.truetype(font, font_size)
    
    boxes = widthremaining // boxwidth
    box_list = []
    for i in range(boxes):
        left = x + i * boxwidth
        box_list.append((left, y))

    for ulcorner in box_list:
        xoff = randint(0, randxoffset)
        yoff = randint(0, randyoffset)
        letter = message[randint(0, len(message) - 1)]
        draw.text((ulcorner[0] + xoff, ulcorner[1] + yoff),
                  letter, font=fnt, fill = 0)


    for i in range(boxes):
        shardx = randint(xmargin, pane.size[0]-xmargin-boxwidth)
        shardy = randint(ymargin, pane.size[1]-ymargin-boxheight/2)
        shard = pane.crop((shardx, shardy, shardx+boxwidth, shardy+boxheight/2))
        pane.paste(shard, (x+i*boxwidth, y+boxheight/2))

    return pane


def etch(message, img_format=None,
        font="/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf",
        font_size=30, glasswidth = 500, charsperline=20, boxheight=20, boxwidth=20,
        spacewidth=13, randomoffset=True, randxoffset=4, randyoffset=5,
        xmargin=30, ymargin=30):
    """
    Return Python Imaging Library Image with text 'etched' on it

    Defaults to bmp image
    """

    # TODO decouple the font path, figure out how to pass it in as an object or
    # otherwise specify it

    # Create a provisional glass height. We will adjust the glass to fit the message later.
    glassheight = (len(message) // (glasswidth // boxwidth) + 5) * boxheight
    pane = Image.new('RGB', (glasswidth + 2*xmargin, glassheight + 2*ymargin),
                     color=(255, 255, 255))
    draw = ImageDraw.Draw(pane)
    fnt = ImageFont.truetype(font, font_size)

    # Configure the positioning of the letters in the message.
    left = xmargin
    top = ymargin
    box_list = [(left, top)]
    for i in range(len(message) - 1):
        if message[i + 1] == " ":
            left += spacewidth
        else:
            left += boxwidth
        if left + boxwidth > glasswidth:
            top += boxheight
            left = xmargin
        box_list.append((left, top))

    letter = iter(message)
    for ulcorner in box_list:
        if randomoffset: # Possibly offset letters inside their boxes
            xoff = randint(0, randxoffset)
            yoff = randint(0, randyoffset)
        else:
            xoff = 0
            yoff = 0
        draw.text((ulcorner[0]+xoff, ulcorner[1]+yoff), letter.next(), font=fnt, fill=0)
    
    if top != ymargin:
        # Fill up the remainder of the space on the bottom.
        pane = fill_remaining(pane, message, boxwidth, boxheight,
                              randxoffset, randyoffset, font_size, xmargin, ymargin,
                              widthremaining=glasswidth-(box_list[-1][0]+boxwidth),
                              x=box_list[-1][0]+boxwidth,
                              y=box_list[-1][1])

    glass = crop_to_text(pane)
    glasswidth = glass.getbbox()[2]
    glassheight = glass.getbbox()[3]
    pane = Image.new('RGB', (glasswidth + 2*xmargin, glassheight + 2*ymargin), color=(255, 255, 255))
    pane.paste(glass, (xmargin, ymargin))

    return pane

def recenter_warped(pane, params):
    """
    Center an image of text from an external program in a pane with given margins.
    
    Requires black text on a white background.
    """

    xmargin, ymargin = params['xmargin'], params['ymargin']

    glass = crop_to_text(pane)
    glasswidth = glass.getbbox()[2]
    glassheight = glass.getbbox()[3]
    pane = Image.new('RGB', (glasswidth + 2*xmargin, glassheight + 2*ymargin), color=(255, 255, 255))
    pane.paste(glass, (xmargin, ymargin))

    return pane

