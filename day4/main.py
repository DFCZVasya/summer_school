users = []

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
    while 1:
        print("enter password")
        password1 = input()
        if len(password1) > 3:
            break
        print("password is too short")
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
    f.close()


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
    while 1:                         
        if in_user(user):            
            break                    
    
def print_user_list(_):
    for user in users:
        print("{} {}\n".format(user[0], user[1]))
    return 0

def change_name(user):
    while 1:
        print("enter new name")
        new_name = input()
        flag, _ = compare_user_name(new_name)
        if not flag:
            break
        print("bad name, try again!")
    user[0] = new_name
    return 0
        

def change_password(user):
    while 1:
        print("enter new password")
        password1 = input()
        if len(password1) > 3:
            break
        print("password is too short")
    while 1:
        print("repeat password")
        password2 = input()
        if password1 == password2:
            break
    user[1] = password1
    return 0

def log_out(_):
    return 1

def in_user(user):
    mods = {'1': print_user_list,
           '2': change_name,
           '3': change_password,
           '4': log_out}

    print("1 - user list")
    print("2 - change name")
    print("3 - change password")
    print("4 - log out")

    mod = get_mode_number(mods)
    if mod:
        return mods[mod](user)
    else:
        print("wrong number!") 


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
