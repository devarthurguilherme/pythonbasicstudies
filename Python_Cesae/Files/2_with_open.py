#More common is using WITH
with open("Python_Cesae\Files\example.txt", "r") as file:
    conteudo = file.read()
    print(conteudo)