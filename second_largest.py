arr = list(map(int, input().split()))
Fmax = arr[0]
Smax = arr[1]
if Fmax < Smax :
    Fmax, Smax = Smax, Fmax
for i in range(len(arr)):
    if arr[i] > Fmax:
        Smax = Fmax
        Fmax = arr[i]
        
    elif arr[i] >Smax and arr[i]<Fmax:
        Smax = arr[i]
print(Fmax, Smax)