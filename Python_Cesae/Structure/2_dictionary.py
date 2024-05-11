arthurGuilherme = {
    "Name": "Arthur Guilherme",
    "Age": "32",
    "City": "Vila Nova de Famalicão"
}

def checkKey(dictionary, key):
    if str(key) in dictionary:
        print(dictionary[key])
    else:
        print("Try again!")

def showAll(dictionary):
    for key in dictionary:
        print(f"key {key} value {dictionary[key]}")

def addKey(dictionary, key, value):
    dictionary[key] = value
    print(dictionary)

print("*"*100)

print(arthurGuilherme["Name"])
print(arthurGuilherme["Age"])
print(arthurGuilherme["City"])

print("*"*100)
checkKey(arthurGuilherme, "Name")
checkKey(arthurGuilherme, "Weight")

print("*"*100)
showAll(arthurGuilherme)

print("*"*100)
addKey(arthurGuilherme, "Weight", "95")

#3