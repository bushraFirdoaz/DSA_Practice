
s = input()

freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

chars = list(freq.keys())

for i in range(len(chars)):
    for j in range(i + 1, len(chars)):

        if freq[chars[i]] < freq[chars[j]]:
            chars[i], chars[j] = chars[j], chars[i]

        elif freq[chars[i]] == freq[chars[j]]:
            if chars[i] > chars[j]:
                chars[i], chars[j] = chars[j], chars[i]

result = ""

for ch in chars:
    result += ch * freq[ch]

print(result)
