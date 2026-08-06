student_grade = {"jack" : 50, "terry" : 62, "marie" : 78, "ben" : 47, "emma" : 80}
total = 0
for i in student_grade:
    total += student_grade[i]
avg = total / 5
print("student grade : ",student_grade)
print("class average : ",avg)
print("highest performer : ",max(student_grade, key = student_grade.get))
print("lowest performer : ",min(student_grade, key = student_grade.get))
name = input("Enter the student's name to search in class : ")
if student_grade.get(name) is not None:
    print(name, "scored : ",student_grade.get(name))
else:
    print(name, "not found")
