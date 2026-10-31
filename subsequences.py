def printsubsequences(ind, ds, arr, n):
    if ind ==n:
        print(ds)
        return
    ds.append(arr[ind])
    printsubsequences(ind+1, ds, arr, n)
    ds.pop()
    printsubsequences(ind+1, ds, arr, n)
arr = [3,1,2]
n = len(arr)
ds =[]
printsubsequences(0, ds, arr, n)