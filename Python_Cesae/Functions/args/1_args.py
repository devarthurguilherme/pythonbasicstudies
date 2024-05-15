#Args allow to pass a different argument numbers
#They will ALWAYS be in a TUPLE, it doesn't depend of hte arguments numbers
#Remember, Tuple is like a "Constant List" because it doesn't accept a new element
def plus(*args):
    return sum(args)

# Function with different arguments numbers:
print(plus(1, 2, 3))       # out: 6
print(plus(4, 5, 6, 7, 8)) # out: 30
print(plus(10))            # out: 10

#Doubt: Do I have to pass same argument type?
#Answer: Yes
def showArguments(*args):
    for arg in args:
        print(arg)

showArguments("A", "r", "t", "h", "u", "r")

print("*"*100)

#Just a TUPLE here
def withoutArgument(*args):
    print(args)
    print(type(args))

withoutArgument()
