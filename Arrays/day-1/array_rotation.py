# method-1 (Using temp variable)
# Time complexity is O(n)
# space complexity is O(d)


def rotation(arr,d,n):
    temp = []
    k = n-int(d)
    for i in range(d):
        temp.append(arr[i])
    for i in range(k):
        arr[i] = arr[i+d]
    for i in range(d):
        arr[k+i] = temp[i]

    return arr

arr = [1,2,3,4,5,6]
d = 5
n = len(arr)
rotation(arr,d,n)
print('The 1st method output ',arr)
print()
print()


# method-2 (Rotate one by one)
# time complexity is O(n*d)
# space complexity is O(1)

def onebyone(arr, d, n):
    for i in range(d):
        leftrotatebyone(arr,n)


def leftrotatebyone(arr,n):
    temp = arr[0]
    for i in range(n-1):
        arr[i] = arr[i+1]
    arr[n-1] = temp






if __name__ == '__main__':
    arr = [1,2,3,4,5,6]
    n = len(arr)
    d = 5
    onebyone(arr,d,n)
    print('2nd method output ',arr)
    print()
    print()


# method-3 (Juggling algorithm)
# time compelxity O(n)
# auxilary space O(1)

def leftrotate(arr,d,n):
    d = d%n
    g = gcd(d,n)
    for i in range(g):
        temp = arr[i]
        j = i
        while True:
            k = j + d
            if k >= n:
                k = k - n
            if k == i:
                break
            arr[j] = arr[k]
            j = k
        arr[j] = temp


def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)



if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    d = 3
    n = len(arr)
    leftrotate(arr,d,n)
    print('third method output is ',arr)
    print()
    print()



# cyclicilly rotate array one by one
# time complexity O(n)
# space complexity O(1)

def rotate(arr, n):
    x = arr[n - 1]

    for i in range(n - 1, 0, -1):
        arr[i] = arr[i - 1];

    arr[0] = x;


# Driver function
arr = [1, 2, 3, 4, 5]
n = len(arr)
print("Given array is")
for i in range(0, n):
    print(arr[i], end=' ')

rotate(arr, n)

print("\nRotated array is")
for i in range(0, n):
    print(arr[i], end=' ') 













