arr = list(map(int, input().split()))
target = int(input())

l = 0
h = len(arr) - 1

while l <= h:
    mid = (l + h) // 2

    if arr[mid] == target:
        print(mid)
        break

    elif arr[mid] > target:
        h = mid - 1

    else:
        l = mid + 1

else:
    print(l)