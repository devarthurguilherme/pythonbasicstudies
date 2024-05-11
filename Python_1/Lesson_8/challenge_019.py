from random import randint, choice

students = ["Arthur", "Thavea", "Jr", "Lea"]
student = randint(0, len(students) - 1)
chosen = choice(students)

print("The student is", students[student])
print("The student is", chosen)
