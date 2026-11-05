arr = list(map(int, input().split()))
n = int(input())
for i in range(len(arr)):
    if arr[i] == n:
        print("Found the value of n in arr",i, n)
    