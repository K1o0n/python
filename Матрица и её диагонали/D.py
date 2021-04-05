a = int(input())
b = [[int(j) for j in input().split()] for i in range(a)]
o = int(input())
for t in range(a - abs(o)):
    if o > 0:
        print(b[t + o][t], end=' ')
    else:
        print(b[t][t - o], end=' ')