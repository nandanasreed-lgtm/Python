student_names = []
student_marks = []
grades = []
print("Enter student names: ")
for i in range(5):
    name = input(f"Student {i+1} name: ")
    marks = int(input(f"Enter marks for {name} (out of 100): "))
    student_names.append(name)
    student_marks.append(marks)
    if marks >= 90:
        grades.append("A")
    elif marks >=70:
        grades.append("B")
    elif marks >=50:
        grades.append("C")
    else:
        grades.append("F")

print("\nStudent Marks List:")
for i in range(5):
    print(f"{student_names[i]}: {student_marks[i]} - Grade: {grades[i]}")
