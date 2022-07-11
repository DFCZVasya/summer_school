users = [["test", "test"], ["admin", "admin"]]
filename = "data_base.csv"

def registration():
    name = input("enter name: ")
    password1 = input("enter password: ")
    password2 = input("enter password again: ")
    if password1 != password2:
        print("passwords are not equal!")
        return False

    for user in users:
        if name == user[0]:
            print("name is already taken!")
            return False
    users.append([name, password1])
    print(users)
    return True    

def login():
    name = input("enter name: ")
    password = input("enter password: ")
    for user in users:
        if name == user[0] and password == user[1]:
            return True
    return False

def readDataBase():
    









def main():
    print("1 - login")
    print("2 - regestration")
    result = input()
    if result == "1":
        print(login())
    elif result == "2":
        print(registration())
    else:
        print("bad input")

# Доделать меню используя результаты прошлых задач и 
# предлжить зарегистрированному пользователю использовать одну из 
# функций (arithmeticm, is_year_leap, square, season)
#
#
def menu():
    pass

if __name__=="__main__":
    main()