arr = list(map(int, input().split()))
n = len(arr)
res =[]
for i in range(n):
    prod =1
    for j in range(n):
        if i!=j:
            prod*=arr[j]
    res.append(prod)
print(res)