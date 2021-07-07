a = [ 1, 1, 1, 2, 3, 4, 4, 5] # 1 2 3 4 5
t = a[0] - 1 # 0
for num in a:
    if num != t:
        print(num)
        t = num

