arr = list(map(int, input().split()))
n= int(input())
l, h = 0, len(arr)-1
while l<=h:
    mid = (l+h)//2
    if arr[mid] == n:
        print(mid)
        break
    elif arr[mid] > n:
        h = mid-1
    elif arr[mid] < n:
        l = mid+1
else:
    print("Not found")