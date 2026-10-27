ar = list(map(int, input().split()))
n = len(ar)
k = int(input())
Sum =0
for i in range(k):
    Sum +=ar[i]
Maxsum = Sum
l =0
r =k
while r<n:
    Sum = Sum+ar[l]
    l+=1
    Sum +=ar[r]
    r+=1
    
    Maxsum = max(Maxsum, Sum)
print(Maxsum)