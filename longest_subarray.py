arr = list(map(int, input().split()))
k=int(input())
max_len =0
for i in range(len(arr)):
    Sum =0
    for j in range(i, len(arr)):
        Sum+=arr[j]
        if Sum<=k:
            max_len = max(max_len, j-i+1)
print(max_len)