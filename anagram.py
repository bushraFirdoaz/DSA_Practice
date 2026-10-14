s1 = input()
s2 = input()
if len(s1) != len(s2):
    print("Not anagram")
elif sorted(s1) != sorted(s2):
    print("Not anagram")
else:
    print("Anagram")