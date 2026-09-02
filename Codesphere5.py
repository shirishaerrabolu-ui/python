print("===== DAILY ACTIVITY PLANNER =====")

name = input("Enter your name: ")
day = input("What day is it? ")
mood = input("How are you feeling today? (happy/tired/excited): ")

print("\nHello", name + "!")
print("Today is", day)

if mood == "happy":
    activity = "Go outside, play a game, or spend time with friends."
elif mood == "tired":
    activity = "Take some rest, read a book, and do light activities."
elif mood == "excited":
    activity = "Try something fun like sports, gaming, or a creative project."
else:
    activity = "Have a balanced day with study, exercise, and relaxation."

print("\n===== YOUR DAILY PLAN =====")
print("Morning:  Study and complete homework")
print("Afternoon: Exercise or play")
print("Evening:", activity)
print("Night:  Relax and prepare for tomorrow")

print("\nHave a great day,", name + "!")