from array import array

snacks = {"Chips", "Biscuits", "Juice"}
snacks.add("Sandwich")

print("Available Snacks:", snacks)

student_snacks = {"Juice", "Chips", "Cake"}

print("Common Snacks:", snacks.intersection(student_snacks))

counts = array('i', [10, 5, 8, 12])
counts.append(6)

print("Snack Counts:", counts)
print("Chips Count:", counts.count(10))

counts.reverse()
print("Reversed Counts:", counts)