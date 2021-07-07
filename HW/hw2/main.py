import math

def task1():
    a = int(input())
    print(a-1, a+1)

def task2():
    x,y = int(input()), int(input())
    print(math.sqrt(x*x + y*y))

def main():
    task1()
    task2()

if __name__ == "__main__":
    main()