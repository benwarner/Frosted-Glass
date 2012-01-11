import Image

import random



def convert_point(pt):
    pt = pt ^ (random.randint(0,1)*255)

def convert_list(_list, frostyness):
    for x in range(len(_list)):
        _list[x] = _list[x] ^ int(frostyness*random.random()//2)

def convert_to_01(data):
    return [1 if 0 < x else 0 for x in data]

def convert_to_255(data):
    return [255 if 0 < x else 0 for x in data]

def frost(pane, frostyness = 2.6):
    """
    Xors image with random string, returns XORed version
    """

    bwimg = pane.convert('1')


    d = bwimg.getdata()
    import pdb
#    pdb.set_trace()
    bindata = convert_to_01(d)

    convert_list(bindata, frostyness)

    data255 = convert_to_255(bindata)
    bwimg.putdata(data255)

    return bwimg

# results = process()

# f = [int(random.randint(0,3)//2) for x in range(20)]
