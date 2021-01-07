def findodd(l):
    res = []
    for x in l:
        count = l.count(x)
        if count % 2 != 0:
            res.append(x)
    return res

l = [1,1,1,1,2,3,4,3,4,5]
print(findodd(l))