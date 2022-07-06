users = [["test", "test"], ["admin", "admin"]]


def registration():
    name = input("enter name: ")
    password1 = input("enter password: ")
    password2 = input("enter password again: ")
    if password1 == password2:
        print("passwords are not equal!")
        return False

    for user in users:
        if name == user[0]:
            print("name is already taken!")
            return False


    users.append([name, password1])
    return True    

def login():
    name = input("enter name: ")
    password = input("enter password: ")
    for user in users:
        if name == user[0] and password == user[1]:
            return True
    return False

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


if __name__=="__main__":
    main()