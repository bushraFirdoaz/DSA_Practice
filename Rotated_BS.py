arr = list(map(int ,input().split()))
target = int(input())
l = 0
h = len(arr)-1
while l<=h:
    mid = (l+h)//2
    if arr[mid] == target:
        print("Target Found", mid)
        break
    elif arr[l] < arr[mid]:
        if arr[l] <target < arr[mid]:
            h = mid-1
        else:
            l = mid+1
    else:
        if arr[mid] < target < arr[h]:
            l = mid+1
        else:
            h = mid-1