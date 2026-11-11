arr = list(map(int, input().split()))
i =0
for j in range(1, len(arr)):
    if arr[j] != arr[i]:
        i+=1
        arr[i] = arr[j]
print(i+1)
print(*arr[:i+1])