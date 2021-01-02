def getsmaller(l,x):
    res = []
    for i in range(len(l)):
        if l[i] < x:
            res.append(l[i])
    return res
l = [1,23,4,5,3,2,6,7,89,899,943]
x = 50
print(getsmaller(l,x))