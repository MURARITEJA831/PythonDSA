def getevenorodd(l):
    even = []
    odd = []
    for i in range(len(l)):
        if l[i] % 2 == 0:
            even.append(l[i])
        else:
            odd.append(l[i])
    return even,odd
l = [1,2,3,4,5]
even, odd = getevenorodd(l)
print('even numbers is: ',even)
print()
print('odd numbers is: ',odd)