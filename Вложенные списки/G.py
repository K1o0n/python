a, b = input()
dicta = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7}
a = dicta[a]
b= 8- int(b)
pole = [['Q' if (a==i and b == j) else '*' if ((i==a) or (j==b) or (a-b == i-j) or (a+b == i+j)) else '.' for i in range(8) ]for j in range(8)]
for h in range(8):
	print(*pole[h])