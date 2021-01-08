def BinarySearch(arr,start,end,x):
    while start <= end:
        mid = (start+end) // 2
        if arr[mid] == x:
            return mid+1
        elif arr[mid] < x:
            start = mid+1
        else:
            end = mid-1
    return -1


if __name__ == "__main__":
    arr = [1,2,3,4,5,7,8,9]
    start = 0
    end = len(arr) - 1
    x = 25
    print('The position of the element is ',BinarySearch(arr,start,end,x))