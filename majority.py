def majority(arr):
    
    n = len(arr)
    for i in range(n):
        cnt = 0
        for j in range(n):
            if arr[i] == arr[j]:
                cnt+=1
        if cnt >= n//2:
            print(arr[i])
            break
arr = list(map(int, input().split()))
majority(arr)
