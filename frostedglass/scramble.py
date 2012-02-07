import random

def genperm(brokenglass, seed):
    """
    Returns a random permutation with the same length as brokenglass
    based on the given seed
    """
    
    random.seed(seed)
    perm = range(len(brokenglass))
    random.shuffle(perm) # This shuffles the list in place.
    
    return perm


def scramble(brokenglass, key):
    """
    Permute ordered list of tiles into random sequence

    The dustpan holds the random collection of tiles.
    """

    perm = genperm(brokenglass, seed=key)

    dustpan = []
    for i in perm:
        dustpan.append(brokenglass[i])

    return dustpan


def unscramble(brokenglass, key):
    """
    Unscramble a list of tiles according to a key, the inverse of scramble

    Returns an unscrambled list of images.
    """

    # Find the correct permutation to unscramble the message using the key
    perm = genperm(brokenglass, seed=key)

    # Rearrange the shards so that they can be glued in sequence.
    orderedtaggedshards = sorted(zip(perm, dustpan))
    orderedshards = []
    for i in orderedtaggedshards:
        orderedshards.append(i[1])

    return orderedshards


