print("=== Smart School Day Planner ===")

# Step 2: Get inputs
day = input("Enter the day: ").strip().title()
weather = input("Enter the weather (sunny/rainy/cloudy): ").strip().lower()
homework = input("Is your homework done? (yes/no): ").strip().lower()

# Step 3: Plan header
print(f"\n=== Plan for {day} ===")

# Step 4: Classify the day
if day in ("Saturday", "Sunday"):
    print("Day type : Weekend - enjoy your free time!")
elif day == "Monday":
    print("Day type : First day of the week.")
elif day == "Friday":
    print("Day type : Last school day.")
elif day in ("Tuesday", "Wednesday", "Thursday"):
    print("Day type : Regular school day.")
else:
    print("Day type : Day not recognised.")

if weather == "sunny" and homework == "yes":
    print("After school: Head to the park!")

# Step 6: OR operator
if weather == "rainy" or weather == "cloudy":
    print("Weather tip : Pack your umbrella!")

# Step 7: NOT operator
if not (homework == "yes"):
    print("Homework : Not done yet. Finish it before getting out!!")

# Step 8: Combine AND + OR + NOT
if weather == "rainy" and not (homework == "yes"):
    print("Best plan : Stay in, finish homework first.")
elif weather == "sunny" and homework == "yes" and not (day in ("Saturday", "Sunday")):
    print("Best plan : All set for a great school day!")
elif day in ("Saturday", "Sunday") and weather == "sunny":
    print("Best plan : Perfect weekend - head outside!")
else:
    print("Best plan : Take it one step at a time!")

# Step 9: Closing message
print("\nPlan complete! Have a wonderful day!")



