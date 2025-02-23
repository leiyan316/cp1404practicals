"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""

def main():
    number_of_month = get_months()
    incomes = get_income(number_of_month)
    calculate_total_income(number_of_month,incomes)

def get_income(number_of_month):
    """get and display income for each month"""
    incomes = []
    for i in range(1, number_of_month + 1):
        income = float(input("Enter income for month " + str(i) + ": "))
        incomes.append(income)
    print("\nIncome Report\n-------------")
    return incomes

def get_months():
    """get number of months"""
    number_of_month = int(input(f"How many months?:"))
    return number_of_month

def calculate_total_income(number_of_month,incomes):
    """calculate and display total income"""
    total = 0
    for i in range(1, number_of_month + 1):
        income = incomes[i - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(i, income, total))


main()