n = int(input())
arr = list(map(int, input().split( )))
Max = arr[0]
Min = arr[0]
for i in range(1, n):
    if arr[i]>Max:
        Max = arr[i]
    if arr[i]<Min:
        Min = arr[i]
print(Max)
print(Min)