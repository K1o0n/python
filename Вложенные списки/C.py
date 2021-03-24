n, m = list(map(int, input().split()))
snow = [['.' if (j%2==1 and i%2 ==1) or (j%2==0 and i%2 ==0) else '*' if (j%2==0 and i%2 ==1) else '*' for j in range(m)] for i in range(n)]
for h in range(n):
    print(*snow[h])