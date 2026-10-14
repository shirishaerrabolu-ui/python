
import random

def random_fun_calculator():
    print("===================================")
    print("       🎲 RANDOM FUN CALCULATOR")
    print("===================================")

    while True:
        print("\nChoose an option:")
        print("1. Random Number")
        print("2. Random Addition")
        print("3. Random Multiplication")
        print("4. Lucky Number Game")
        print("5. Magic Math Challenge")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            number = random.randint(1, 100)
            print("Your random number is:", number)

        elif choice == "2":
            a = random.randint(1, 50)
            b = random.randint(1, 50)
            print(f"\n{a} + {b} = {a + b}")

        elif choice == "3":
            a = random.randint(1, 20)
            b = random.randint(1, 20)
            print(f"\n{a} x {b} = {a * b}")

        elif choice == "4":
            lucky_number = random.randint(1, 10)
            guess = int(input("Guess a number between 1 and 10: "))

            print("The lucky number was:", lucky_number)

            if guess == lucky_number:
                print("🎉 Amazing! You guessed correctly!")
            else:
                print("😄 Better luck next time!")

        elif choice == "5":
            number = random.randint(1, 20)
            print("Your magic number is:", number)
            print("Double it:", number * 2)
            print("Add 10:", number * 2 + 10)
            print("Divide by 2:", (number * 2 + 10) / 2)
            print("Subtract your original number:", 
                  (number * 2 + 10) / 2 - number)

        elif choice == "6":
            print("Thanks for playing! Goodbye! 🎮")
            break

        else:
            print("Invalid choice! Please try again.")

random_fun_calculator()
