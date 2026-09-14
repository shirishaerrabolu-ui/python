# ATM Cash Dispenser

serving = True

customers_served = 0
total_dispensed = 0

note_500 = 0
note_200 = 0
note_100 = 0
note_50 = 0
note_20 = 0
note_10 = 0

notes = [500, 200, 100, 50, 20, 10]

while serving:

    name = input("Enter customer name: ")
    amount = int(input("Enter withdrawal amount: "))

    # Check for invalid amount
    if amount <= 0:
        print("Invalid amount. Try again.\n")
        continue

    if amount % 10 != 0:
        print("Amount must be a multiple of 10.\n")
        continue

    remaining = amount
    idx = 0

    # Nested while loop
    while idx < len(notes):

        value = notes[idx]
        count = remaining // value

        if count > 0:

            remaining = remaining % value

            if value == 500:
                note_500 += count
            elif value == 200:
                note_200 += count
            elif value == 100:
                note_100 += count
            elif value == 50:
                note_50 += count
            elif value == 20:
                note_20 += count
            elif value == 10:
                note_10 += count

        idx += 1

    customers_served += 1
    total_dispensed += amount

    print("\n₹", amount, "dispensed to", name)
    print("Withdrawal successful!\n")

    answer = input("Is there another customer? (yes/no): ")

    if answer.lower() != "yes":
        serving = False


# Daily denomination report
print("\n===== DAILY DENOMINATION REPORT =====")
print("Customers served:", customers_served)
print("Total amount dispensed: ₹", total_dispensed)

denominations = [
    ("₹500", note_500),
    ("₹200", note_200),
    ("₹100", note_100),
    ("₹50", note_50),
    ("₹20", note_20),
    ("₹10", note_10)
]

# Outer for loop
for name, count in denominations:

    print("\n", name, "notes:", count)

    # Inner for loop
    for i in range(count):
        print("=", end="")

    print()

print("\n===== ATM SESSION COMPLETE =====")
print("Thank you!")