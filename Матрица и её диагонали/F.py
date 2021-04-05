def pr(arr):
    for z in range(c):
        for y in range(a):
            print(b[y][z], end = ' ')
        print()


a, c  = map(int,input().split())
b = [[int(j) for j in input().split()] for i in range(a)]
pr(b)