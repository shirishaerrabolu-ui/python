print("================================")
print("   PARKING TICKET PAYMENT HELPER")
print("================================")

ticket_amount = float(input("Enter parking ticket amount: ₹"))

def calculate_change(paid, amount):
    if paid > amount:
        return paid - amount
    elif paid == amount:
        pass
    return 0

paid_amount = 0

print("\nEnter coins one at a time.")
print("Valid coins: ₹1, ₹2, ₹5, ₹10")
print("Enter 0 when you are finished.")

while paid_amount < ticket_amount:
    coin = float(input("Insert coin: ₹"))

    if coin == 0:
        break

    if coin not in [1, 2, 5, 10]:
        print("Invalid coin! Try again.")
        continue

    paid_amount += coin
    print("Amount paid: ₹", paid_amount)

if paid_amount >= ticket_amount:
    change = calculate_change(paid_amount, ticket_amount)

    print("\n========== RECEIPT ==========")
    print("Ticket Amount: ₹", ticket_amount)
    print("Amount Paid: ₹", paid_amount)

    if change > 0:
        print("Change: ₹", change)
    else:
        pass
        print("No change needed.")

    print("Payment successful!")
else:
    print("\nPayment cancelled.")
    print("Amount collected: ₹", paid_amount)
    print("Remaining amount: ₹", ticket_amount - paid_amount)