def main():
    check_user()
    numbers = get_numbers()
    display_target_number(numbers)

def check_user():
    """check user's name"""
    sernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
    username = input("Enter your name: ")
    while username not in sernames:
        print("Access denied")
        username = input("Enter your name: ")
    print("Access granted")


def get_numbers():
    """get numbers from user"""
    numbers = []
    for i in range(5):
        number = int(input("Number: "))
        numbers.append(number)
    return numbers

def display_target_number(numbers):
    """display first/last/smallest/largest/average number"""
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers) / len(numbers):.1f}")


main()