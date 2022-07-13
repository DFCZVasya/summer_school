import random

n = int(input())
m = int(input())

matrix = []
line = []
for i in range(n):
    for j in range(m):
        line.append(random.randint(-100, 100))
    matrix.append(line.copy())
    line = []

print(matrix)

file = open("test.txt", "w")
for i in range(n):
    for j in range(m):
        file.write(str(matrix[i][j]) + " ")
    file.write("\n")

