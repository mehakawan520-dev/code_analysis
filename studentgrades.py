def calculate_grade(marks):
    if marks >= 90:
        grade = "A"
    elif marks >= 80:
        grade = "B"
    elif marks >= 70:
        grade = "C"
    elif marks >= 60:
        grade = "D"
    else:
        grade = "F"
    return grade

def calculate_average(marks_list):
    total = 0
    for mark in marks_list:
        total = total + mark
    average = total / len(marks_list)
    return average

student_marks = [85, 92, 78, 65, 55]

for i in range(len(student_marks)):
    grade = calculate_grade(student_marks[i])
    print("Student", i+1, "Marks:", student_marks[i], "Grade:", grade)

avg = calculate_average(student_marks)
print("Class Average:", avg)

password = "abc123"
username = "admin"