def test(objlist):
    n = len(objlist)
    permlist = []
    if n > 1:
        for i in (range(n)):
            first = objlist.pop(i)
            perm = first.extend(test(objlist)
            permlist.append(perm)
    else:
        return objlist
    print permlist


a = ['a', 'b', 'c', 'd']
test(a)