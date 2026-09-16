print("Diamond Pattern")

rowSize = int(input("Enter the diamond size: "))

if rowSize % 2 == 0:
    halfDiamRow = rowSize // 2
else:
    halfDiamRow = (rowSize // 2) + 1

space = halfDiamRow - 1
number = 1

for i in range(1, halfDiamRow + 1):
    space = 0
halfDiamRow = 10

for i in range(1, halfDiamRow + 1):

    for j in range(1, space + 1):
        print(" ", end=" ")

    space = space + 1

    number = 1

    for j in range(1, 2 * (halfDiamRow - i) + 1):
        print(number, end=" ")
        number = number + 1

    print()

space = space - 1

for i in range(1, halfDiamRow + 1):

    for j in range(1, space + 1):
        print(" ", end=" ")

    space = space + 1

    number = 1

    for j in range(1, 2 * i):
        print(number, end=" ")
        number = number + 1

    print()