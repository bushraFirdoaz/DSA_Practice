arr = list(map(int,input().split()))
i,j =0,0
while i<len(arr):
    if arr[i] !=0:
        arr[i], arr[j] = arr[j], arr[i]
        j+=1
    i+=1
print(arr)