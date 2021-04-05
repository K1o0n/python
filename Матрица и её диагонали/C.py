def pr(arr):
    for z in range(len(arr)):
        print(*arr[z])


a, n = map(int, input().split())
b = [[int(j) for j in input().split()] for i in range(a)]
o, p = map(int, input().split())
for t in range(a):
    b[t][o], b[t][p] = b[t][p], b[t][o]
pr(b)