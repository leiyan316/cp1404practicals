DISCOUNT = 0.9

number_of_items = int(input("Number of items: "))
while number_of_items < 0 :
    print("Invalid number")
    number_of_items = int(input("Number of items: "))
total_price = 0
for i in range(number_of_items):
    price = float(input(f"Price of item {i + 1}: "))
    total_price = total_price + price
if total_price > 100:
    total_price = total_price * DISCOUNT
print(f"Total price for {number_of_items} items is ${total_price:.2f}")