def Sum(n):
    if n==0:
        return 0
    return Sum(n-1) + n
print(Sum(5))