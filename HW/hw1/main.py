a = [1, 2, 3 , 4, 5, 6]

for i in range(len(a)):
    if a[i] % 2 == 0:
        a[i] = 0

print(a)