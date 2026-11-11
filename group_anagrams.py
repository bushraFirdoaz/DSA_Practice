n = int(input())
groups ={}
for i in range(n):
    word = input().strip()
    key = ''.join(sorted(word))
    if key not in groups:
        groups[key] = []
    groups[key].append(word)
for group in groups.values():
    group.sort()
    print(*group)