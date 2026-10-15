n = int(input())
arr = list(map(int, input().split()))

Sum_arr=0
Sum_n = n*(n+1)//2
for i in range(len(arr)):
    Sum_arr += arr[i]
missing = Sum_n - Sum_arr
print(missing)