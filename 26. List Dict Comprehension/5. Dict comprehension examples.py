import random

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleonor', 'Freddie']
student_scores = {student: random.randint(1, 100) for student in names}

print(student_scores)


passed_students = {student: score for (student, score) in student_scores.items() if score > 50}
print(passed_students)
