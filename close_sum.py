arr = list(map(int, input().split()))
target = int(input())
arr.sort()
n = len(arr)
minDiff = float('inf')
closeSum = 0
for i in range(n-2):
    l,r = i+1, n-1
    while l<r:
        Sum = arr[i]+arr[l]+arr[r]
        currD = abs(target-Sum)
        if currD<minDiff:
            minDiff = currD
            closeSum = Sum
        if Sum < target:
            l+=1
        elif Sum > target:
            r-=1
        else:
            closeSum = Sum
            break
print(closeSum)