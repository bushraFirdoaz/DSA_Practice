def permutations(arr, ds, visited):

    if len(ds) == len(arr):
        print(ds)
        return

    for i in range(len(arr)):

        if visited[i] == False:

            visited[i] = True
            ds.append(arr[i])

            permutations(arr, ds, visited)

            ds.pop()
            visited[i] = False

arr = [1, 2, 3]
ds = []
visited = [False] * len(arr)
permutations(arr, ds, visited)