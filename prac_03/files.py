name = input("Enter your name: ")
with open("name.txt", "w") as file:
    file.write(name)

with open("name.txt", "r") as file:
    name = file.read().strip()
print(f"Hi {name}!")

with open("numbers.txt", "r") as file:
    number1 = int(file.readline().strip())
    number2 = int(file.readline().strip())
    result = number1 + number2
    print(f"The sum of the first two numbers is: {result}")

with open("numbers.txt", "r") as file:
    total = 0
    for line in file:
        total += int(line.strip())
    print(f"The total of all numbers is: {total}")