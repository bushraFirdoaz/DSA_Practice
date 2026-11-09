x = int(input())
arr1 = list(map(int, input().split()))
y = int(input())
arr2 = list(map(int, input().split()))
arr1.sort()
arr2.sort()
cnt = 0
i =0
j=0
while i<x and j<y:
    if arr1[i] <= arr2[j]:
        cnt+=1
        i+=1
        j+=1
    else:
        j+=1
print(cnt)
