arr = list(map(int, input().split()))
visited =[]
for i in range(len(arr)):
    if arr[i] in visited:
        continue
    cnt=0
    for j in range(len(arr)):
        if arr[i] == arr[j]:
            cnt+=1
    
    
    print(arr[i], "->", cnt)
    visited.append(arr[i])