
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Cannot divide by zero."
    return a / b

def power(a, b):
    return a ** b

def remainder(a, b):
    if b == 0:
        return "Error! Cannot divide by zero."
    return a % b

while True:
    print("\n==============================")
    print("      FUNCTION CALCULATOR")
    print("==============================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Remainder")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "7":
        print("Thank you for using the calculator!")
        break

    if choice in ["1", "2", "3", "4", "5", "6"]:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if choice == "1":
                result = add(num1, num2)
            elif choice == "2":
                result = subtract(num1, num2)
            elif choice == "3":
                result = multiply(num1, num2)
            elif choice == "4":
                result = divide(num1, num2)
            elif choice == "5":
                result = power(num1, num2)
            elif choice == "6":
                result = remainder(num1, num2)

            print("Result:", result)

        except ValueError:
            print("Please enter valid numbers!")

    else:
        print("Invalid choice! Please try again.")