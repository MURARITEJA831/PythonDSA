def listcomprehension(l):
    even = [i for i in range(1,11) if i % 2 ==0]
    odd = [x for x in range(1,11) if x % 2 != 0]
    #for sets we use curly braces
    s = {x for x in range(1,11) if x % 2 == 0}
    # for dictinary we can use same as sets like curly braces
    # but we need to use colon 
    dic = {x: x**2 for x in l}
    return even,odd,s,dic

l = [1,2,3,4,5]
even, odd,s,dic= listcomprehension(l)
print('even list is: ',even)
print('odd list is: ',odd)
print('set items is: ',s)
print('dictionary items is: ',dic)
print()
print('........Dictionary reversing......')
d1 = {101:'gfg',102:'fgf',103:'logicmojo'}
d2 = {v:k for (k,v) in d1.items()}
print(d2)