print("====================================")
print("       🌴 HOLIDAY ACTIVITY PLANNER 🌴")
print("====================================")

name = input("Enter your name: ")

print("\nChoose the weather:")
print("1. Sunny")
print("2. Rainy")
print("3. Cloudy")

weather = int(input("Enter your choice (1-3): "))

print("\nHow much free time do you have?")
print("1. Less than 2 hours")
print("2. 2-4 hours")
print("3. More than 4 hours")

time = int(input("Enter your choice (1-3): "))

print("\nDo you want an outdoor activity?")
print("yes / no")

outdoor = input("Enter your choice: ").lower()

print("\n------------------------------------")
print("       YOUR HOLIDAY PLAN")
print("------------------------------------")

if weather == 1 and outdoor == "yes":
    if time == 1:
        activity = "Go for a short bike ride 🚲"
    elif time == 2:
        activity = "Play cricket or football ⚽"
    else:
        activity = "Go on a long outdoor adventure 🏕️"

elif weather == 2 or outdoor == "no":
    if time == 1:
        activity = "Read a book 📖"
    elif time == 2:
        activity = "Watch a movie 🎬"
    else:
        activity = "Play games or learn coding 💻"

elif weather == 3 and time >= 2:
    activity = "Go for a walk and take some cool photos 📸"

else:
    activity = "Do some drawing, gaming, or creative work 🎨"

print("Name:", name)
print("Recommended Activity:", activity)

print("------------------------------------")
print("Have an awesome holiday, " + name + "! 😎")
print("====================================")