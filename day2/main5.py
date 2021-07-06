def get_currensy_key(currensy_cods):
    for cod in currensy_cods:
        print(cod)
    print("enter currensy key: ", end = ' ')

    key = input()

    if key in currensy_cods:
        return key
    else:
        return 0

def get_money():
    money = int(input("enter sum of money you want to change: "))
    if money > 0:
        return money
    return 0

def main():
    EUR = 87
    USD = 73
    YEN = 15
    currensy_cods = ["EUR 400", "USD 401", "YEN 500"]

    money = get_money()
    if not money:
        print("ERROR!")
        return

    key = get_currensy_key(currensy_cods)
    if key:
        if key == currensy_cods[0]:
            print("to recive {0:0.2f} EUR".format(money/EUR))
        elif key == currensy_cods[1]:
            print("to recive {0:0.2f} USD".format(money/USD))
        elif key == currensy_cods[2]:
            print("to recive {0:0.2f} YEN".format(money/YEN))
    else:
        print("ERROR!")

if __name__ == "__main__":
    main()