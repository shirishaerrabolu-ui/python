print("======================================")
print("       GROCERY BILLING QUEUE")
print("======================================")

customers = int(input("Enter number of customers: "))

queue = []

# Add customers to the queue
for i in range(customers):
    name = input(f"\nEnter name of customer {i + 1}: ")
    queue.append(name)

print("\n======================================")
print("          BILLING STARTED")
print("======================================")

# Process each customer
for customer in queue:

    print(f"\nNow billing: {customer}")

    items = int(input("Enter number of items: "))

    total = 0

    # Enter prices of items
    for i in range(items):
        price = float(input(f"Enter price of item {i + 1}: ₹"))
        total = total + price

    print("\n---------- BILL ----------")
    print("Customer:", customer)
    print("Items:", items)
    print("Total: ₹", total)

    # Discount
    if total >= 2000:
        discount = total * 0.10
        print("Discount: ₹", discount)
        total = total - discount

    elif total >= 1000:
        discount = total * 0.05
        print("Discount: ₹", discount)
        total = total - discount

    else:
        print("Discount: ₹0")

    print("Final Bill: ₹", total)
    print("--------------------------")

print("\n======================================")
print("       ALL CUSTOMERS BILLED!")
print("======================================")