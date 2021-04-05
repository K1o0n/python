def Transpose(arr):
    for z in range(a):
        for y in range(a):
            print(b[-(y+1)][z], end = ' ')
        print()


a = int(input())
b = [[int(j) for j in input().split()] for i in range(a)]
Transpose(b)