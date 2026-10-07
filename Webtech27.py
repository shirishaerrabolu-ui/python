import random

while True:
    print("================================")
    print("      ROCK PAPER SCISSORS")
    print("================================")

    player_action = input("Choose rock, paper, or scissors: ").lower()

    computer_number = random.randint(1, 3)

    if computer_number == 1:
        computer_action = "rock"
    elif computer_number == 2:
        computer_action = "paper"
    else:
        computer_action = "scissors"



    print(f"You chose: {player_action}")
    print(f"Computer chose: {computer_action}")


    if player_action == computer_action:
        print("It's a tie!")
    elif player_action == "rock" and computer_action == "scissors":
        print("You win!")
    elif player_action == "paper" and computer_action == "rock":
        print("You win!")
    elif player_action == "scissors" and computer_action == "paper":
        print("You win!")
    else:
        print("You lose!")

    again = input("Do you want to play again?? (y/n): ").lower()

    if again != "y":
        print("Thanks for playing!!!!!!!!!!!!!!!")
        break

