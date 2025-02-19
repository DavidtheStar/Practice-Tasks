"""Make a second version of the program above (average marks) and change it so
that all names and marks are added to a list. In addition to the output
produced in the original version, this version should also calculate and
print each student's name and a 'University' style grade. """
students = []
best_student =""
best_mark =-1
total_marks = 0
student_count = 0
# This function was created by chatGPT, to remember how things work etc
def get_grade(mark):
    if mark >= 90:
        return "A+"
    elif mark >= 85:
        return "A"
    elif mark >= 80:
        return "A-"
    elif mark >= 75:
        return "B+"
    elif mark >= 70:
        return "B"
    elif mark >= 65:
        return "B-"
    elif mark >= 60:
        return "C+"
    elif mark >= 55:
        return "C"
    elif mark >= 50:
        return "C-"
    elif mark >= 40:
        return "D"
    else:
        return "E"
while True:
    student_name = input("What is the Students name?: ").title()

    if student_name =="X":
        break
    student_grade = int(input(f"What is {student_name}'s grade?: "))

    if student_grade < 0 or student_grade > 100:
        print("That is an invalid grade. Please enter grade between 1-100: ")
        continue

    students.append((student_name, student_grade))

    if student_grade > best_mark:
        best_mark = student_grade
        best_student = student_name

    total_marks += student_grade

if students:
    average_mark = total_marks / len(students)
    print(f"\nBest Student: {best_student} with a mark of {best_mark}")
    print(f"Average mark for all students: {average_mark:.2f}\n")

    print("Student Grades:")
    for name, mark in students:
        print(f"{name}: {mark} - {get_grade(mark)}")
else:
    print("No students were entered.")
