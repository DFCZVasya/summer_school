import random
import matrixPrint
A = []
for i in range(0,3):
    A.append([])
    for j in range(0,3):
        A[i].append(random.randint(0,10))

matrixPrint.printMatrix(A)

print(
    A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])
    -A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])
    +A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0]))
