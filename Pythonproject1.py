secret = random.randint(1, 50)



attempts = 0


while attempts < 5:
    guess = int(input("Enter your guess: "))
    attempts += 1


    if guess == secret:
        print("You guessed it!! ")
        break



    difference = abs(secret - guess)

    if difference <= 3:
        print("Hot")
    elif difference <= 7:
        print("Warm")
    elif difference <= 15:
        print("Cold")
    else:
        print("ICE COLD!!")


    print("❤️"  * (5 - attempts))


    if attempts == 5 and guess !=
    secret:
       print("Game over! The secret number was", secret)               
       