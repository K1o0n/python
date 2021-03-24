a, b = str(input())
dicta = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
a = dicta[a]
b = int(b)
pole = [['K' if (i == a and j == (8 - b)) else '*' if (
        (i == a - 1 and j == 10 - b) or (i == a - 1 and j == 6 - b) or (i == a + 1 and j == 6 - b) or (
        i == a + 1 and j == 10 - b) or (i == a + 2 and j == 7 - b) or (i == a - 2 and j == 7 - b) or (
                    i == a + 2 and j == 9 - b) or (i == a-2 and j == 9-b)) else '.' for i in
         range(8)] for j in range(8)]

for h in range(8):
    print(*pole[h])
