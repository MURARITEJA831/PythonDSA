def swap(a,b,arr):
    arr[a],arr[b] = arr[b],arr[a]
    return arr


arr=[1,2,3,4,5]
start = 0
end = len(arr)-1
while start <= end:
    arr = swap(start,end,arr)
    start += 1
    end -= 1
print(arr)

