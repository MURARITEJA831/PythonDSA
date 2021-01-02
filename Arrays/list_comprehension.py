def listcomprehension(l):
    even = [i for i in range(1,11) if i % 2 ==0]
    odd = [x for x in range(1,11) if x % 2 != 0]
    return even,odd

l = [1,2,3,4,5]
even, odd= listcomprehension(l)
print('even list is: ',even)
print('odd list is: ',odd)