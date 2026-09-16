print("======================================")
print("       HOMEWORK COMPLETION TRACKER")
print("======================================")

students = int(input("Enter number of students: "))

completed = 0
not_completed = 0

for i in range(students):
    print("\nStudent", i + 1)

    name = input("Enter student name: ")
    homework = int(input("Enter number of homework tasks: "))

    finished = 0

    for j in range(homework):
        status = input(
            f"Was task {j + 1} completed? (yes/no): "
        ).lower()

        if status == "yes":
            finished = finished + 1

    print("\n--------------------------")
    print("Student:", name)
    print("Completed:", finished, "/", homework)

    if finished == homework:
        print("Status: All homework completed!")
        completed = completed + 1

    elif finished > 0:
        print("Status: Homework partially completed!")
        not_completed = not_completed + 1

    else:
        print("Status: No homework completed!")
        not_completed = not_completed + 1

    print("--------------------------")

print("\n======================================")
print("             SUMMARY")
print("======================================")

print("Students with all homework completed:", completed)
print("Students needing more work:", not_completed)

print("======================================")
print("       TRACKING COMPLETE!")
print("======================================")

