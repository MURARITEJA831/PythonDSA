def merge_sort(arr):
    if len(arr) <= 1:
        return
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    merge_sort(left)
    merge_sort(right)

    merge_sorted(left,right,arr)

def merge_sorted(a,b,arr):
    len_a = len(a)
    len_b = len(b)
    i = j = k = 0
    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            arr[k] = a[i]
            i += 1
        else:
            arr[k] = b[j]
            j += 1
        k += 1
    while i < len_a:
        arr[k] = a[i]
        i += 1
        k += 1
    while j < len_b:
        arr[k] = b[j]
        j += 1
        k += 1


if __name__ == "__main__":
    testcases = [
        [2,85,45,69,1,258,-15],
        [],
        [1,2,3,4,5],
        [5,4,3,2,1,6]
    ]
    for arr in testcases:
        merge_sort(arr)
        print(arr)