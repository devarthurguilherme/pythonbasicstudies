#Calc the average of several numbers
def calcAverage(*args):
    if len(args) == 0:
        return 0
    
    return sum(args) / len(args)

print(calcAverage(2, 4, 6, 8, 10))
print(calcAverage(3, 7, 15, 20, 12))
print(calcAverage(4, 5, 7, 10, 1))