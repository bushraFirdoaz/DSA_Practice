arr = list(map(int, input().split()))
pro = 0
max_pro = 0
min_price =arr[0]
for i in range(len(arr)):
    if arr[i] <= min_price:
        min_price = arr[i]
    else:
        pro = arr[i] - min_price
        if pro>max_pro:
            max_pro = pro

print(max_pro)
            