import random
print([i for i in range(100) if i in [random.randint(0,99) for j in range(100)] and i in [random.randint(0,99) for j in range(100)]])