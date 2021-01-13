# method-1(Linear Search)
# time complexity is O(n)
# space complexity is O(1)

def RotationCount(arr):
    if arr[0] > arr[len(arr)-1]:
        if arr[1] < arr[0]:
            return 1
        min = arr[0]
        for i in range(len(arr)):
            if min < arr[i]:
                min = arr[i]
                min_index = (len(arr)-1) - i
        return min_index
    else:
        return 0



if __name__ == '__main__':
    arr = [1,2,3,4]
    print(RotationCount(arr),' rotations')

# method-2(Binary Search)
# time complexity is O(logn) with constant space

def RotationCountBinarySearch(arr,l,h):
    if arr[l] < arr[h]:
        return 0
    if l == h:
        return l
    mid = (l+h)//2
    if l < mid and arr[mid] < arr[mid-1]:
        return mid
    if h > mid and arr[mid+1] < arr[mid]:
        return mid+1
    if arr[l] < arr[mid]:
        return RotationCountBinarySearch(arr,mid+1,h)
    return RotationCountBinarySearch(arr,l,mid-1)

if __name__ == '__main__':
    arr = [3,4,5,6,1]
    print(len(arr)-RotationCountBinarySearch(arr,0,len(arr)-1),' rotation/rotations takes place')