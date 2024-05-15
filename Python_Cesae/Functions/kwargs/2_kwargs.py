#Print key and values of a dictionary
def printKeyValue(**kwargs):
    for key, value in kwargs.items():
        print(f"key: {key} {value} <-- value")
    print(kwargs)
    print(type(kwargs))

printKeyValue(name="Arthur", age=32, city="Vila Nova de Famalicão")
