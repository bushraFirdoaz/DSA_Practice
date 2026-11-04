def unique(arr):
    
    for i in range(len(arr)):
        cnt =0
        for j in range(len(arr)):
            
            if arr[i] == arr[j]:
                cnt+=1
        if cnt ==1:
            print(arr[i])


arr = list(map(int, input().split()))
unique(arr)
    