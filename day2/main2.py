EUR = 87
USD = 73
all_money = int(input("enter sum of money you want to change: "))

if all_money < 0:
    print("ERROR!")
    exit()

key = input("enter value key (400 - EUR, 401 - USD): ")
#print(all_money, key)

if key == "400":
    print("to recive {0:9.2f} EUR".format(all_money/EUR))
elif key == "401":
    print("to recive {0:9.2f} USD".format(all_money/USD))
else:
    print("{} - wrong value".format(key))