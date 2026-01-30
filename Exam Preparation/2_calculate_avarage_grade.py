num = int(input())

grades = []

for i in range(num):
    student_grades = float(input())
    grades.append(student_grades)

list_of_grades = sum(grades)
avarage_grade = list_of_grades/ num

print(f"{avarage_grade:.2f}")