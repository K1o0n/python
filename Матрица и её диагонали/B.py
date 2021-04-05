def pr(arr):
    for z in range(len(arr)):
        print(*arr[z])
a = int(input())
b = [[0 if i+j < a-1 else 1 if i+j == a-1 else 2 for i in range(a) ] for j in range(a)]
pr(b)