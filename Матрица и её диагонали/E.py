def pr(arr):
    for z in range(len(arr)):
        print(*arr[z])


a = int(input())
b = [[int(j) for j in input().split()] for i in range(a)]
for t in range(a):
    b[t][t], b[a-1-t][t] = b[a-1-t][t], b[t][t]
pr(b)