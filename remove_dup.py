s = input()
res = ""
for i in range(len(s)):
    if s[i] not in res:
        res+=s[i]
print(res)