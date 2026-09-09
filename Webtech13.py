total_chores = 4
original_count = total_chores

print(f"You have {original_count} chores to finish today!\n")

completed_count = 0
chore_num = 1

# Chore checklist
while chore_num <= total_chores:

    if chore_num == 1:
        next_chore = "Make your Bed"
    elif chore_num == 2:
        next_chore = "Feed the pet"
    elif chore_num == 3:
        next_chore = "Take out the trash"
    else:
        next_chore = "Wash the dishes"

    answer = input(f"Have you finished: {next_chore}? (yes/no): ")

    if answer.lower() == "yes":
        completed_count += 1
        chore_num += 1
        print("Great job! Chore completed.\n")
    else:
        print("Okay, finish it and check again!\n")

    print("Chores remaining:", total_chores - completed_count)
    print()

# All chores are complete
print("===== ALL CHORES COMPLETE! =====")
print("Great work finishing your entire checklist today!\n")


# Safe infinite loop demonstration
print("Now let's safely peek at the infinite loop....")

test_value = 0
safety_counter = 0

while test_value <= 0:
    print("This condition never ends, so this would run forever!")

    safety_counter += 1

    if safety_counter == 3:
        print("(Stopping here on purpose - a real infinite loop never stops on its own!)")
        break

print("\nProgram finished safely!")