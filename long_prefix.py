a = list(input().split())
short = min(a, key = len)
prefix = ""
for i in range(len(short)):
    for j in range(len(a)):
        if a[j][i] != short[i]:
            break
    else:
        prefix +=short[i]
        continue
    break
print(prefix) 