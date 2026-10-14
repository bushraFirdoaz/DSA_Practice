s = input()
vow = ("a","e","i","o","u")
vcnt, ccnt =0,0
for i in range(len(s)):
    if s[i] in vow:
        vcnt +=1
    else:
        ccnt+=1
print(vcnt, ccnt)