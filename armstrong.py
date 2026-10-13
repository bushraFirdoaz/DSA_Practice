n = int(input())
total =0
org1 =n
org2 =n
cnt=0
Sum=0
while n>0:
    n = n//10
    cnt +=1

while org1>0:
    digit = org1%10
    org1 = org1//10
    Sum = Sum+digit**cnt

if (Sum==org2):
    print("Armstrong")
else:
    print("Not armstrong")