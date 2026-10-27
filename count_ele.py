arr = list(map(int, input().split()))
freq ={}
for num in arr:
    if num in freq:
        freq[num] +=1
    else:
        freq[num] =1
for num in freq:
    if freq[num] ==1:
        print(num)
   