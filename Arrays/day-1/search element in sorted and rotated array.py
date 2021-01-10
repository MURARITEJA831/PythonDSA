

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