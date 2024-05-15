#Find bigger number
def biggerNumber(*args):
    if len(args) == 0:
        return "Nothing here!"
    return max(args)

print(biggerNumber())
print(biggerNumber(7, 3, 4, 2, 0, 11, 9))