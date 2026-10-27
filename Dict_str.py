S = input()
freq = {}
for s in S:
    if s in freq:
        freq[s]+=1
    else:
        freq[s]=1
print(freq)
