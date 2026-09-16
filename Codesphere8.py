
print("================================")
print("       LOOP ART DESIGNER")
print("================================")

rows = int(input("Enter the number of rows: "))

print("\nChoose your design:")
print("1. Star Triangle")
print("2. Number Triangle")
print("3. Pyramid")
print("4. Diamond")
print("5. Square")

choice = int(input("Enter your choice: "))

print("\nYour Art:\n")

# 1. Star Triangle
if choice == 1:
    for i in range(1, rows + 1):
        for j in range(i):
            print("*", end=" ")
        print()

# 2. Number Triangle
elif choice == 2:
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

# 3. Pyramid
elif choice == 3:
    for i in range(1, rows + 1):
        for j in range(rows - i):
            print(" ", end=" ")

        for j in range(2 * i - 1):
            print("*", end=" ")

        print()

# 4. Diamond
elif choice == 4:
    # Top half
    for i in range(1, rows + 1):
        for j in range(rows - i):
            print(" ", end=" ")

        for j in range(2 * i - 1):
            print("*", end=" ")

        print()

    # Bottom half
    for i in range(rows - 1, 0, -1):
        for j in range(rows - i):
            print(" ", end=" ")

        for j in range(2 * i - 1):
            print("*", end=" ")

        print()

# 5. Square
elif choice == 5:
    for i in range(rows):
        for j in range(rows):
            print("#", end=" ")

        print()

else:
    print("Invalid choice!")

print("\n================================")
print("       Thanks for designing!")
print("================================")