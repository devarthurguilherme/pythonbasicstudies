#Now, Use it with a existing list
smallStudentsList = ["Arthur", "Alex", "Nathan", "Alex Jr"]
bigStudentsList = ["... several names before"]

#Without List Comprehension
for student in smallStudentsList:
    bigStudentsList.append(student)

print(bigStudentsList)
print("*"*100)
#With List Comprehension, BUT using the last list
otherSmallStudentList = ["Pedro", "Tiago", "João"]
bigStudentsList.extend(student for student in otherSmallStudentList)
print(bigStudentsList)