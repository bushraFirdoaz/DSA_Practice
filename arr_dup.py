def remove_duplicate(arr):
    uni = set()
    for i in range(len(arr)):
        if arr[i] not in uni:
            uni.add(arr[i])
    return uni
arr = list(map(int, input().split()))
print(remove_duplicate(arr))

