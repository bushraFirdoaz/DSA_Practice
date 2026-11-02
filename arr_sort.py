def arr_sort(arr):
    n = len(arr)
    isSorted = True
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            isSorted = False
    if isSorted:
        print("Sorted")
    else:
        print("Not sorted")
arr = list(map(int, input().split()))
arr_sort(arr)