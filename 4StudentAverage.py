"""Your English teacher wants a program to keep track of their student
marks and grades.Write a program which takes, as input, the student's name
and an exam mark -between 0 and 100.The program should keep asking for input
until "X" is entered as the student name. The program should then output the
name and mark of best student, as well as  average mark for all students."""

best_student =""
best_mark =-1
total_marks = 0
student_count = 0
while True:
    student_name = input("What is the Students name?: ").title()

    if student_name =="X":
        break
    student_grade = int(input(f"What is {student_name}'s grade?: "))

    if student_grade < 0 or student_grade > 100:
        print("That is an invalid grade. Please enter grade between 1-100: ")
        continue

    if student_grade > best_mark:
        best_mark = student_grade
        best_student = student_name

    total_marks += student_grade
    student_count += 1

if student_count > 0:
    average_mark = total_marks / student_count
    print(f"\nBest Student: {best_student} with a mark of {best_mark}")
    print(f"Average mark for all students: {average_mark:.2f}")
else:
    print("No students were entered.")