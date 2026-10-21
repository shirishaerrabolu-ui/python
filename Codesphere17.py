print("===================================")
print("       WEEKLY HABIT TRACKER")
print("===================================")

days = ["Monday", "Tuesday", "Wednesday", "Thursday",
        "Friday", "Saturday", "Sunday"]

habits = ["Wake Up Early", "Exercise", "Read Books",
          "Drink Enough Water", "Study Python"]

tracker = {}

for habit in habits:
    tracker[habit] = []
    print("\nHabit:", habit)

    for day in days:
        while True:
            status = input(day + " (yes/no): ").lower()

            if status == "yes" or status == "no":
                tracker[habit].append(status)
                break
            else:
                print("Please enter yes or no.")

print("\n===================================")
print("         WEEKLY REPORT")
print("===================================")

total_completed = 0
total_possible = len(habits) * len(days)

for habit in habits:
    completed = tracker[habit].count("yes")
    total_completed += completed

    print("\nHabit:", habit)
    print("Completed:", completed, "out of 7 days")
    print("Progress:", round(completed / 7 * 100), "%")

    for i in range(len(days)):
        print(days[i] + ": " + tracker[habit][i])

print("\n===================================")
print("         FINAL SUMMARY")
print("===================================")

print("Total habits:", len(habits))
print("Total completed:", total_completed, "out of", total_possible)
print("Overall progress:", round(total_completed / total_possible * 100), "%")

if total_completed == total_possible:
    print("Amazing! You completed every habit!")
elif total_completed >= total_possible / 2:
    print("Great work! Keep building your habits!")
else:
    print("Keep going! Every small step counts!")

print("===================================")