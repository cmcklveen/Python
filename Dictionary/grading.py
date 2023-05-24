# TODO 1.Creat an empty dictionary called student_grades

student_grades = {}


student_grades = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

# TODO 2. Write code below to add the grades to student_grades

for student in student_grades:
    score = student_grades[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    if score > 80:
        student_grades[student] =  "Exceeds Expectations"
    if score > 70:
        student_grades[student] = "Acceptable"
    if score > 60:
        student_grades[student] = "Failed"

print




