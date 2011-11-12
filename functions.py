class shard(object):
    """shards are rectangular chunks of pixels that are rearranged into scrambled or unscrambled images."""
   
    def __init__(self, row = 0, col = 0):
        """shard position"""
        
        self.row = row
        self.col = col

    def __dimensions__(self, height = 10, width = 10):
        """The number of pixels tall and wide of the shard."""
        
        self.height = height
        self.width = width

    def get_pixels(stuff): #I'm still not sure how to do this. It needs to use the information about its row, column, height, and width.
        """Makes a serialized copy of the pixels that fall within the area of the shard (a tuple?)."""





class glass(object):
    """The glass is the portion of the image that contains the message and rearranged."""

    def __init__(self, glassheight = 200, glasswidth = 100):
        """The message area. Will need to be adjusted in order to fit the message."""
    
    def write_message(message_file, font = courier, font_size = 10, vertical_pad = 4, horizontal_pad = 4):
        """Reads in a text file and writes it into the message area."""

        for line in open(message_file, encoding = "utf8"):
            for letter in line:
                # Write the letter! It needs to be written in a little box which is the height and width of a normal letter plus the vertical and horizontal pad. It will be offset from it's normal position by a random number between 0 and the pad. (Be sure to use secure random number generation.)

    def etch(shardheight = 10, shardwidth = 10):
        """Returns a list of shard objects (not rearranged)."""
        etching = []

        try:
            for row in range(0, glassheight, shardheight):
                for col in range(0, glasswidth, shardwidth):
                    new_shard = shard(shardwidth, shardheight)
                    new_shard.get_pixels(row, col) 
                    etching.append(new_shard)
            return etching
        except DimensionError: #I still need to create this kind of error. It may be that the shards don't fit evenly in the glass.
            print "uh-oh!"
    
    def show_etching(etching):
        """Display the shards, in the order given by the list 'etching', with a red border so the user can see how big they are."""
       
    def frost(contrast_ratio):
        """Blur the background and letters by randomly darkening and lightening pixels"""
        for pixel in image: # 'image' is a serialized image (which I think is a tuple or list of the values of pixels).
            # stuff

        
    def shatter(etching, key):
        """Takes an etching and permutes its shards according to the key."""

        dustpan = itertools.permutations(etching) #This needs to choose the permutation based on the key (somehow).
        print "CRASH!" # :) 
        return dustpan 


def generate_key(bits):
    """Generate a symmetric key of size 'bits'"""

"""If you can't tell already, I still don't know much about oo-programming in python. This still needs to be improved."""
