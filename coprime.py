a = int(input())
b = int(input())
n = min(a,b)
cnt=0
for i in range(1, n+1):
    if a%i==0 and b%i==0:
        cnt+=1
if cnt>1:
    print("Not coprimes")
else:
    print("Co-primes")