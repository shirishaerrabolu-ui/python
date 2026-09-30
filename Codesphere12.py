print("================================")
print("      BILL & SEATING HELPER")
print("================================")

bill = float(input("Enter the total bill: ₹"))
people = int(input("Enter the number of people: "))

tip = float(input("Enter tip percentage: "))

tip_amount = bill * tip / 100
total_bill = bill + tip_amount
each_person = total_bill / people

print("\n========== BILL ==========")
print("Original Bill: ₹", bill)
print("Tip Amount: ₹", tip_amount)
print("Total Bill: ₹", total_bill)
print("Each Person Pays: ₹", each_person)

print("\n========== SEATING ==========")

tables = int(input("Enter number of tables: "))
seats_per_table = int(input("Enter seats per table: "))

total_seats = tables * seats_per_table

if people <= total_seats:
    print("Everyone can be seated!")
    empty_seats = total_seats - people
    print("Empty seats:", empty_seats)
else:
    extra_people = people - total_seats
    print("Not enough seats!")
    print("Extra people:", extra_people)

print("\nThank you for using the Bill & Seating Helper!")