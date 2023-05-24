student_heights = input("Please input a list of student heights separated by a space: ").split()
total_height = 0
total_students = 0

for height in student_heights:
    total_height += int(height)

for student in student_heights:
    total_students += 1
    # print(student)

student_height_average = round(total_height / total_students)

    
print(f"The student heights you inputed are: {student_heights}")

print(f"The total student heights is {total_height}")

print(f"The number of students you entered heights for is {total_students}")

print(f"The average of the students heights is {student_height_average}")

