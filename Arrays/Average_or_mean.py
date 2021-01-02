def average(l):
    sum = 0
    for i in range(len(l)):
        sum += l[i]
    return sum/len(l)

n = int(input('Enter length of the list: '))
l = list(map(int,input('Enter items: ').split()))[:n]
print(average(l))