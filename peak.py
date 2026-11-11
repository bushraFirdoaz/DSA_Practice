arr = list(map(int, input().split()))
n = len(arr)
if arr[0] > arr[1] :
    print(0)
if arr[n-1] > arr[n-2]:
    print(n-1)
for i in range(1, n):
    
    if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
        print(i)
         