import random

fileName = "test.txt"

file = open(fileName, "w")

for i in range(10):
    file.write(str(random.randint(0,1000)) + ',')

file.close()

file = open(fileName, "r")

a = file.read()
a = a.split(",")
a.pop()
for i in range(len(a)):
    a[i] = int(a[i])
print(a)
file.close()