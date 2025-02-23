import random

MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_LINE = 6


def main():
    num_quick_picks = int(input("How many quick picks? "))
    for i in range(num_quick_picks):
        quick_pick = generate_quick_pick()
        print_quick_pick(quick_pick)


def generate_quick_pick():
    """generate a single quick pick"""
    quick_pick = []
    while len(quick_pick) < NUMBERS_PER_LINE:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        if number not in quick_pick:
            quick_pick.append(number)
    quick_pick.sort()
    return quick_pick


def print_quick_pick(quick_pick):
    """display a single quick pick with numbers aligned neatly."""
    for number in quick_pick:
        print(f"{number:2}", end=" ")


main()