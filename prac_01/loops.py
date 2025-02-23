for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a
print("\na. Count in 10s from 0 to 100:")
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# b
print("\nb. Count down from 20 to 1:")
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# c
print("\nc. Print n stars:")
n = int(input("Number of stars: "))
for _ in range(n):
    print('*', end='')
print()

# d
print("\nd. Print n lines of increasing stars:")
n = int(input("Number of stars: "))
for i in range(1, n + 1):
    print('*' * i)