n, m = list(map(int, input().split()))
a = [[int(j) for j in input().split()] for i in range(n)]
d, e = 0, 0
c = a[0][0]
for i in range(n):
    for j in range(m):
        if a[i][j] > c:
            c = a[i][j]
            d, e = i, j
print(d, e)