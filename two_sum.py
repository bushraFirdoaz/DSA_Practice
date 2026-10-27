arr = list(map(int, input().split()))
Sum = int(input())
freq={}
for i in range(len(arr)):
    tar = Sum - arr[i]
    if tar in freq:
        print(freq[tar], i)
        
    freq[arr[i]]=i
    