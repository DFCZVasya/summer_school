def get_numbers():
    a, b = int(input()), int(input())
    return a, b

def get_sign(all_signs):
    sign = input()
    if sign in all_signs:
        return sign
    else:
        return 0

def main():
    all_signs = ['+', '-', '*', '/', '**']

    a,b = get_numbers()

    expressions = {'+': a+b, 
                   '-': a-b,
                   '*': a*b,
                   '/': a/b if b else print("ERROR!"),
                   '**': a**b}

    sign = get_sign(all_signs)
    if sign:
        print(expressions[sign])
    else:
        print("ERROR!")



if __name__ == "__main__":
    main()