n = int(input())
snow = [['*' if i == j or i == n - j - 1 or i == n // 2 or j == n // 2 else '.' for j in range(n)] for i in range(n)]
for h in range(n):
    print(*snow[h])