print("======================================")
print("       🍋 LEMONADE STAND 🍋")
print("======================================")


def calculate_total(quantity, price):
    return quantity * price

def calculate_change(payment, total):
    return payment - total


name = input("Enter your name: ")
print("\nHello,",name + "! Welcome to our lemonade stand! 🍋")


quantity = int(input("How many lemonanades would you like?? "))
price = float(input("Enter the price of one lemonade: "))


total = calculate_total(quantity, price)


print("\nYour total is: $", total)


payment= float(input("Enter the amt you are paying: $"))


change = calculate_change(payment, total)

print("\n======================================")
print("             FINAL RECEIPT")
print("======================================")
print("Customer:", name)
print("Lemonades:", quantity)
print("Price each: ₹", price)
print("Total cost: ₹", total)
print("Amount paid: ₹", payment)
print("Change due: ₹", change)
print("--------------------------------------")
print("Thank you,", name + "!")
print("Whope you enjoyed our lemonade!! 🍋")
print("Please visit our stand again! 🍋")
print("====================================")
