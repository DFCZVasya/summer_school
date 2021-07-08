from main import users

def compare_user_name(name):
    print(users)
    for user in users:
        if name == user[0]:
            return 1, user
    return 0, 0

def compare_password(pwd, user):
    if pwd == user[1]:
        return 1
    return 0

if __name__ == "__main__":
    users.append(["test", "test"])
    print(compare_user_name("new"))
    print(compare_user_name("test"))