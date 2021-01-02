#navie approch

def smax(l):
    if len(l) <= 1:
        return None
    lar = getmax(l)
    slar = None
    for x in l:
        if x != lar:
            if slar == None:
                slar = x
            else:
                slar = max(slar, x)
    return slar

def getmax(l):
    res = l[0]
    for i in range(1,len(l)):
        res = max(res,l[i])
    return res

l = [1,2,3,4,5]
print(smax(l))

#efficient solution

def getsecmax(l):
    if len(l) <= 1:
        return None
    lar = l[0]
    slar = None
    for x in l:
        if x > lar:
            slar = lar
            lar = x
        elif x != lar:
            if slar == None or slar < x:
                slar = x
    return slar

l = [1,2,3,4,5,67,89,23]
print(getsecmax(l))
        