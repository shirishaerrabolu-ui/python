
students = {}

while True:
    print("\n1. Add Student")
    print("2. Display Student")
    print("3. Average")
    print("4. Top Scorer")
    print("5. Exit")

    choice = input("Choose:")

    if choice == "1":
        name = input("Name: ")
        marks = int(input("Marks: "))
        students[name] = marks


    elif choice == "2":
        for name, marks in students.items():
            print(name, marks)


    elif choice == "3":
        if students:
            print("Average:", sum(students.values()) / len(students))


    elif choice == "4":
            if students:
                 top = max(students, key=students.get)
                 print("Top Scorer:", top, students[top])


    elif choice == "5": 
         break


    else:
         print("Invalid Choice!!")            
                      