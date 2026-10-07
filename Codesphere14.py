print("================================")
print("     SHOPPING DISCOUNT CALCULATOR")
print("================================")

amount = float(input("Enter your shopping amount: ₹"))

if amount > 5000:
    discount = amount * 0.20
    discount_percent = 20
elif amount > 3000:
    discount = amount * 0.10
    discount_percent = 10
elif amount > 1500:
    discount = amount * 0.05
    discount_percent = 5
else:
    discount = 0
    discount_percent = 0

final_amount = amount - discount

print("\n----------- BILL -----------")
print("Shopping Amount: ₹", amount)
print("Discount:", discount_percent, "%")
print("You Saved: ₹", discount)
print("Final Amount: ₹", final_amount)
print("----------------------------")
print("Thank you for shopping!")
print("Make sure to come again next time!!")