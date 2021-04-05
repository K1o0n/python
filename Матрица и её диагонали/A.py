def pr(arr):
    for z in range(len(arr)):
        print(*arr[z])
a = int(input())
b = [[abs(i) for i in range(-j, a-j)] for j in range(a)]
pr(b)