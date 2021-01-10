# method-1
# O(Logn)
# O(1)

def findpivot(arr,low,high):
    if high < low:
        return -1
    if high == low:
        return high
    mid = int(low+high) // 2
    if mid < high and arr[mid] > arr[mid+1]:
        return mid
    if mid > low and arr[mid] < arr[mid-1]:
        return mid-1
    if arr[low] >= arr[mid]:
        return findpivot(arr,low,mid-1)
    return findpivot(arr,mid+1,high)

def BinarySearch(arr,low,high,x):
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid+1
        else:
            high = mid-1
    return -1

def pivotedBinarySearch(arr,low,high,x):
    pivot = findpivot(arr,low,high)
    if pivot == -1:
        return BinarySearch(arr,low,high,x)
    if arr[pivot] == x:
        return pivot
    if arr[0] <= x:
        return BinarySearch(arr,low,pivot-1,x)
    return BinarySearch(arr,pivot+1,high,x)


arr = [7,8,9,1,2,3,4,5,6]
low = 0
high = len(arr) - 1
x = 5
print('Index of the ',x,' is ',pivotedBinarySearch(arr,low,high,x))

# improvised solution with one traversal
# O(logn)
# O(1)

def search(arr,low,high,x):
    if low > high:
        return -1
    if low == high:
        return low
    mid = (low+high)//2
    if arr[mid] == x:
        return mid
    if arr[low] <= arr[mid]:
        if x >= arr[low] and x <= arr[mid]:
            return search(arr,low,mid-1,x)
        return search(arr,mid+1,high,x)
    if x >= arr[mid] and x <= arr[high]:
        return search(arr,mid+1,high,x)
    return search(arr,low,mid-1,x)


arr = [-1,-2,-3,1,2,3,4,5]
low = 0
high = len(arr)-1
x = 3
print('position of ',x,' is ',search(arr,low,high,x))