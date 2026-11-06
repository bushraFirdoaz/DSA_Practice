arr = list(map(int, input().split()))
target = int(input())
n = len(arr)
arr.sort()
l, h = 0, n-1
first = -1

while l<=h:
    mid = (l+h)//2
    if arr[mid] == target:
        first = mid
        h = mid-1
    elif arr[mid] < target:
        l = mid+1
    else:
        h = mid-1
        
l, h = 0, n-1
last = -1

while l<=h:
    mid = (l+h)//2
    if arr[mid] == target:
        last = mid
        l = mid+1
    elif arr[mid] < target:
        l = mid+1
    else:
        h = mid-1
print(first, last)