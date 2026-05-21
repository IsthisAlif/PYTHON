# Shopping cart program
item = input("What item would you like to buy? ")
price = float(input("What is the price of the item? "))
quantity = int(input("How many of the item would you like to buy? "))

total = price * quantity
total = round(total, 2)
print(f"You have bought {quantity} x {item}/s")
print(f"Your total is ${total}")