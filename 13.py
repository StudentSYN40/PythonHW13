import random

def pl(t):
    for i in t:
        print(*i)

x = int(input())
y = int(input())

matrix_1 = [[random.randint(-100, 100) for i in range(y)] for i in range(x)]
matrix_2 = [[random.randint(-100, 100) for i in range(y)] for i in range(x)]
matrix_3 = [[0 for i in range(y)] for i in range(x)]

for i in range(x):
    for j in range(y):
        matrix_3[i][j] = matrix_1[i][j] + matrix_2[i][j]

pl(matrix_1)
print("+")
pl(matrix_2)
print("=")
pl(matrix_3)