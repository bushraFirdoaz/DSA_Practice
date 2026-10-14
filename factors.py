n = int(input())
ar=[]
for i in range(1, n+1):
    if(n%i==0):
        ar.append(i)
print(ar)
print(len(ar))