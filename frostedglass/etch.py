"""
Transfer a string of text onto an image

Analogy: etching a message on a piece of glass
"""

import Image
import ImageFont, ImageDraw


def etch(message, img_format=None,
        font="/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf",
        font_size=20, x=800, y=600):
    """
    Return PIL  Image with text 'etched' on it

    Defaults to bmp image

    PIL = [Python Imaging Library]
    """
    # TODO decouple the font path, figure out how to pass it in as an object or
    # otherwise specify it

    # TODO decouple the image size parameters: get image size directly from the
    # image object, instead of passing around
    pane = Image.new('RGB', (x, y), color = (255, 255, 255))
    draw = ImageDraw.Draw(pane)
    fnt = ImageFont.truetype(font, font_size)
    draw.text((10,10), message, font=fnt, fill = 0)
    # memory management in python shouldn't be necessary, especially for one off
    # cases like a single image. Commenting this out, until we know otherwise.
    # del draw
    return pane
