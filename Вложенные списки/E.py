h, y = list(map(int, input().split()))
ab = [[str(j) for j in input().split()]for i in range(h)]
p = int(input())
g = 1
stroka = 0
for t in range(h):
    if g != 0:
        a = ''.join(ab[t])
        n = '0' * p
        if a.find(n) != -1:
            g = 0
            stroka = t+1
print(stroka)