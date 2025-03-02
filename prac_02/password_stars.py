PASSWORD_LENGTH = 10

def main():
    get_password()
    print_asterisk()


def print_asterisk():
    print("*" * PASSWORD_LENGTH)


def get_password():
    password = len(input("Enter password:"))
    while password <= PASSWORD_LENGTH:
        print("Invalid password")
        password = len(input("Enter password:"))


main()