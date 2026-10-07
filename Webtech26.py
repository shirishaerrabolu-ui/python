import random

playing = True


secret_number = str(random.randint(0, 9))


print("   NUMBER GAME")
print("Guess the secret number from 0 to 9!!")


while playing:
    guess = input("Enter your guess: ")

    if guess == secret_number:
        print("Congratualations!! You guessed it!")
        print("The secret number was:", secret_number)
        break
    else:
        print("Wrong guess! try again")