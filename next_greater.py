arr = list(map(int, input().split()))
res =[]
for i in range(len(arr)):
    next =-1
    for j in range(i+1, len(arr)):
        if arr[j] > arr[i]:
            next = arr[j]
            res.append(next)
            break
    else:
        res.append(-1)
print(res)
