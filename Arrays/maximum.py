def maximum(l):
    max = l[0]
    for i in range(1,len(l)):
        if max < l[i]:
            max = l[i]
    return max

l = [1,2,3,4,5,67,4,32]
print('maximum element is ',maximum(l))