#Just open file
fileName = "Python_Cesae\Files\example.txt"
file = open(fileName, "r", encoding="utf-8")#open(file.extension, mode, encoding="utf-8")
content = file.read()

print(content)