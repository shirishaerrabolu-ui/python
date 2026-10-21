print("======================================")
print("     STUDENTS MARKS LIST ANALYZER")
print("======================================")

students = []
marks_list = []

n = int(input("Enter the number of students: "))

for i in range(n):
    print("\nStudent", i + 1)

    name = input("Enter student name: ")
    marks = float(input("Enter marks out of 100: "))

    while marks < 0 or marks > 100:
        print("Invalid marks! Enter marks between 0 and 100.")
        marks = float(input("Enter marks again: "))

    students.append(name)
    marks_list.append(marks)

print("\n======================================")
print("          STUDENTS REPORT")
print("======================================")

for i in range(len(students)):
    marks = marks_list[i]

    if marks >= 90:
        grade = "A+"
    elif marks >= 80:
        grade = "A"
    elif marks >= 70:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 40:
        grade = "D"
    else:
        grade = "Fail"

    print("\nName:", students[i])
    print("Marks:", marks, "/ 100")
    print("Grade:", grade)

total = sum(marks_list)
average = total / n

highest = max(marks_list)
lowest = min(marks_list)

top_index = marks_list.index(highest)
low_index = marks_list.index(lowest)

passed = 0
failed = 0

for marks in marks_list: