s1 = input()
s2 = input()
s = set([s1, s2])
if len(s1) == len(s2):
    if s2 in s:
        print("part of rotation")
    else:
        print("Not part of rotation")
    