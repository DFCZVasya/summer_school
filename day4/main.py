users = []
#from compare import *

def compare_user_name(name):
    for user in users:
        if name == user[0]:
            return 1, user
    return 0, 0

def compare_password(pwd, user):
    if pwd == user[1]:
        return 1
    return 0

def add_new_user():
    print("enter user name")
    while 1:
        user_name = input()
        flag, _ = compare_user_name(user_name)
        if not flag:
            break
        print("bad name, try again!")
    
    print("enter password")
    password1 = input()
    while 1:
        print("repeat password")
        password2 = input()
        if password1 == password2:
            break
    
    users.append([user_name, password1])
    f = open("database", 'w')
    for user in users:
        f.write("{} {}\n".format(user[0], user[1]))
    print(users)


def enter():
    print(users)
    while 1:
        print("enter user name")
        flag, user = compare_user_name(input())
        if flag:
            break
        print("no such user")
    while 1:
        print("enter password")
        password = input()
        if compare_password(password, user):
            break
        print("try again")
    print("WELCOME!")
    
def get_mode_number(mods):
    mod = input()
    if mod in mods:
        return mod
    else:
        return 0

def menu():
    mods = {'1': enter,
            '2': add_new_user,
            '3': exit}   
    print("1 - enter")
    print("2 - new user")
    print("3 - exit")

    mod = get_mode_number(mods)
    if mod:
        mods[mod]()
    else:
        print("wrong number!")
    

def main():
    while 1:
        menu()

if __name__ == "__main__":
    f = open("database", 'r')
    users = f.read().split('\n')
    for i in range(len(users)):
        users[i] = users[i].split()
    users.pop(len(users) - 1)
    f.close()
    main()