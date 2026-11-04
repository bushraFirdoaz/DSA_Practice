s = input()
m =list(s)
s =list(s)
for i in range(len(s)//2):
    s[i], s[len(s)-i-1] = s[len(s)-i-1], s[i]
print(s)
if s == m:
    print("Yes, palindrome")
else:
    print("Not palindrome")