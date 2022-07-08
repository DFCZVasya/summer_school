import random
import matrixPrint
A = []
for i in range(0,3):
    A.append([])
    for j in range(0,3):
        A[i].append(random.randint(0,10))
        
matrixPrint.printMatrix(A)
