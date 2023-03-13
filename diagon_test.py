arr = [[1, 2, 3, 2],[4, 5, 5, 4],[ 7, 9, 9, 7], [1, 0, 0, 0]]
n = len(arr)
#print(n)
for i in range(n):
    for j in range(n):
        if i == j:
            #print(i,j)
            pass
for k in range(n):
    for l in range(n):
        if k == l:
            #print(arr[k][n-k-1])
            pass

print(10%5)