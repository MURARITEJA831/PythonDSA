arr = [5,3,4,1,2,6]
x = 3
diff = float('inf')
ans = -1
for i in arr:
    if i-x > 0 and i-x < diff:
        ans = i
        diff = i-x
print(ans)