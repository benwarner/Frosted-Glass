def test(objlist, sofar = None, permlist = None):
    If permlist is None
        permlist = []
    If sofar is None
        sofar = []

    n = len(objlist)
    if n > 1:
        for i in (range(n)):
#            first = objlist.pop(i)
            perm = first.extend(test(objlist, sofar, permlist))
            permlist.append(perm)
    else:
        return objlist
    print permlist


a = ['a', 'b', 'c', 'd']
test(a)
