x = input("Digit anything: ")

print('What is the type? ', type(x))
print('Is a number? ', x.isnumeric())
print('Is a letter? ', x.isalpha())
print('Is a number or letter? ', x.isalnum())
print('Are there just spaces? ', x.isspace())