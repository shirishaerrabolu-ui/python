print("===== LIBRARY VISIT PLANNER =====")

name = input("Enter your name: ")
day = input("Which day will you visit the library? ")
book_type = input("What type of book do you want? (story/science/history): ")
time = input("How many hours will you stay? ")

print("\n===== YOUR LIBRARY PLAN =====")
print("Visitor:", name)
print("Day:", day)
print("Book type:", book_type)
print("Visit duration:", time, "hours")

if book_type == "story":
    print("Plan: Find a story book and enjoy reading.")
elif book_type == "science":
    print("Plan: Explore science books and learn something new.")
elif book_type == "history":
    print("Plan: Read about interesting historical events.")
else:
    print("Plan: Explore different sections of the library.")

print("\nRemember to:")
print("- Keep your voice low.")
print("- Take care of the books.")
print("- Return borrowed books on time.")

print("\nHave a great library visit,", name + "!")