arr = list(map(int, input().split()))

k=int(input())
n = len(arr)
k = k % n

arr = arr[n-k:] + arr[:n-k]

print(arr)