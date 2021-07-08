f = open("database", 'r')
a = f.read().split('\n')
print(a)
for i in range(len(a)):
    a[i] = a[i].split()
print(a)
a.pop(len(a) - 1)
print(a)