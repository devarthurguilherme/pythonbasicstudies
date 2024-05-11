#Modules
from math import sqrt, ceil

n = int(input('Digit a number: '))
root = sqrt(n)

print('Square Root of {} is: {}.'.format(n, ceil(root)))