arr = list(map(int, input().split()))
n = len(arr)
k = int(input())
print(arr[n-k:] + arr[:n-k])

