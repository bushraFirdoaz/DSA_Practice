n = int(input())
isPrime = True


if n<2:
    isPrime = False
else:
    for i in range(2, n):
        if (n%i==0):
            isPrime = False
            break
    
if (isPrime):
    print("Prime")
else:
    print("Not prime")