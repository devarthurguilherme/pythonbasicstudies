smallStudentsList = ["Arthur", "Alex", "Nathan", "Alex Jr"]
bigStudentsList = ["... several names before"]

#Without List Comprehension
for student in smallStudentsList:
    bigStudentsList.append(student)

print(bigStudentsList)
print("*"*100)
#With List Comprehension
otherSmallStudentList = ["Pedro", "Tiago", "João"]
otherBigStutentsList = [student for student in otherSmallStudentList]
print(otherBigStutentsList)