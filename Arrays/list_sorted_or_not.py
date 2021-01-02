#method-1

def orted(l):
    for i in range(1,len(l)):
        if l[i] < l[i-1]:
            return  False
    else:
        return True

l = [10,20,30,15,40]
print(orted(l))

#method-2

li = [1,2,3,4,5,-1]
sl = sorted(li)
if sl == li:
    print('list is sorted')
else:
    print('list is not sorted')