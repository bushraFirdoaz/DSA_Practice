a = int(input())
b = int(input())
num = max(a,b)
while True:
    if num%a ==0 and num%b==0:
        print(num)
        break
    num+=1