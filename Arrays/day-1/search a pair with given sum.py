# using pivot element
# time complexity O(logn)
# auxilary space is O(1)


def pairsum(arr,low,high,n,x):
    r = findpivot(arr,low,high)
    l = (r+1)%n
    while l != r:
        if arr[l]+arr[r] == x:
            return arr[l],arr[r]
        elif arr[l] + arr[r] < x:
            l = (l+1) % n
        else:
            r = (n+r-1)%n
    return False

def findpivot(arr,low,high):
    if low == high or high < low:
        return -1
    mid = (low+high)//2
    if mid > low and arr[mid] < arr[mid-1]:
        return mid-1
    if mid < high and arr[mid] > arr[mid+1]:
        return mid
    if arr[low] <= arr[mid]:
        return findpivot(arr,mid+1,high)
    return findpivot(arr,low,mid-1)

if __name__ == '__main__':
    arr = [3,4,5,6,1,2]
    low = 0
    high = len(arr) - 1
    X = 10
    print(pairsum(arr,low,high,len(arr)-1,X))


# using middle algorithm
# time complexity is O(n)
# auxilary space O(1)

def pairsum2(arr,n,x):
    for i in range(n):
        if arr[i] > arr[i+1]:
            break
    r = i
    l = (i+1) % n
    while l != r:
        if arr[l] + arr[r] == x:
            return arr[l],arr[r]
        if arr[l] + arr[r] < x:
            l = (l+1)%n
        else:
            r = (n+r-1)%n
    return False

if __name__ == '__main__':
    arr = [3,4,5,6,7,1,2]
    x = 10
    n = len(arr)-1
    print(pairsum2(arr,n,x))


# using pivot finding count if pairs having sum

def findpivot1(arr,low,high):
    if high > low or high == low:
        return -1
    mid = (low+high)//2
    if mid > low and arr[mid] < arr[mid-1]:
        return mid-1
    if mid < high and arr[mid] > arr[mid+1]:
        return mid
    if arr[low] <= arr[mid]:
        return findpivot1(arr,mid+1,high)
    return findpivot1(arr,low,mid-1)

def pairscount(arr, x):
    low = 0
    high = len(arr) - 1
    r = findpivot1(arr, low, high)
    l = (r + 1) % n
    cnt = 0
    while l != r:
        if arr[l] + arr[r] == x:
            cnt += 1

            if l == (n + r - 1) % n:
                return cnt
            l = (l+1) % n
            r = (n+r-1) % n
        elif arr[l]+arr[r] < x:
            l = (l + 1) % n
        else:
            r = (n+r-1) % n
    return cnt


if __name__ == '__main__':
    arr = [3,4,5,6,7,8,9,1,2]
    x = 10
    print(pairscount(arr, x))

