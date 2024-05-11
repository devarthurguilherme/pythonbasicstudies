from math import sqrt, pow

c1 = float(input(' Digit leg1: '))
c2 = float(input(' Digit leg2: '))
hypotenuse = sqrt(pow(c1, 2) + pow(c2, 2))

print("The hypotenuse is: {:.2f}".format(hypotenuse))