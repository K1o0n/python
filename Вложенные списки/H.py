a, b = list(map(int, input().split()))
table = [['0' for i in range(b)] for j in range(a)]
score = 0
stroka = 0
for _ in range(b * a):
    if score > b - 1:
        score = 0
        stroka += 1
    table[stroka][score] = stroka * score
    score += 1
for t in range(a):
    for g in range(b):
        print(' ' * (4 - len(str(table[t][g]))) + str(table[t][g]), end='')
    print()
