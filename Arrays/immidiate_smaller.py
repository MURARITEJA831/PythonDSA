arr = [5,4,1,2,3]
x = 4
fst_sml = -1
for i in range(len(arr)):
    if arr[i] < x and fst_sml < arr[i]:
        fst_sml = arr[i]
print(fst_sml)