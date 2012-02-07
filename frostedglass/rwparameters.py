import frost

def makeparameters(shardswide=25, shardstall=15, xmargin=30,
                   ymargin=30, frostyness=.35):
    """
    Make a dictionary of default parameters.
    
    Returns a dictionary.
    """

    params = {'shardswide': shardswide,
     'shardstall': shardstall,
     'xmargin': xmargin,
     'ymargin': ymargin,
     'frostyness': frostyness}

    return params

def writeparameters(pane, params):
    """
    Encode important information in the upper right hand corner of the
    image about the size of the shards in use, the size of the margins
    and the amount of frostyness in order to smoothly decrypt the message.
    """
    
    sw = bin(params['shardswide'])[2:]
    st = bin(params['shardstall'])[2:]
    xm = bin(params['xmargin'])[2:]
    ym = bin(params['ymargin'])[2:]
    fr = bin(int(params['frostyness']*255))[2:]

    # This is an ugly way of doing this, and hopefully can be improved.
    binparams = [sw, st, xm, ym, fr]
    for i in range(len(binparams)):
        leading_zeros = 8 - len(binparams[i])
        zeros = ''
        for zero in range(leading_zeros):
            zeros += '0'
        binparams[i] = zeros + binparams[i]

    (x, y) = (0, 0)
    for var in binparams:
        for pixie in var:
            value = (0, 0, 0) if pixie == '0' else (255, 255, 255)
            pane.putpixel((x, y), value)
            x += 1
        x = 0 # Start at the beginning of the next line.
        y += 1
                
#    # Turn the image into binary data
#    panedata = pane.getdata()
#    bindata = frost.convert_to_01(panedata)
#
#    bindata[0] = sw
#    bindata[8] = st
#    bindata[24] = xm
#    bindata[32] = ym
#    bindata[40] = fr
#
#    # Turn the binary data back into an image
#    data255 = frost.convert_to_255(bindata)
#    pane.putdata(data255)


def readparameters(pane):
    """
    Reads in the parameters encoded in the pixels at the top of the image.
    
    Returns a dictionary containing values for shardswide, shardstall,
    xmargin, ymargin, and frostyness
    """
    
    bindigits = 8 # The number of binary digits encoding each prameter.
    params = {}
    y = 0
    for param in ('shardswide', 'shardstall',
                  'xmargin', 'ymargin', 'frostyness'):
        # This is a really annoying way to do this but I know no other way.
        binstr = ''
        for x in range(bindigits):
            bin_number = 0 if pane.getpixel((x, y)) == (0, 0, 0) else 1
            binstr += str(bin_number)
        params[param] = int(binstr, 2)
        y += 1

    # Covert frostyness back into a decimal
    params['frostyness'] = float(params['frostyness'])/255

    return params
