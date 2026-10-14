s = input()

dig, let1, let2, spec = 0,0,0,0
for i in range(len(s)):
    if s[i] >= "0" and s[i] <= "9":
        dig+=1
    elif (s[i]>= "A" and s[i]<="Z"):
        let1 +=1
    elif (s[i] >="a" and s[i] <="z"):
        let2+=1
    else:
        spec+=1
print(dig, let1, let2, spec)