a = int(input())
n = [[int(j) for j in input().split()]for i in range(a)]
g = 'YES'
for q in range(a):
    for w in range(a):
        if q!=w:
            if n[q][w] != n[w][q]:
                g = 'NO'
                break
print(g)