#Arithmetic Operators
#Alignments
n = 'Arthur'
print('Hello {:20}!'.format(n))
print('Hello {:>20}!'.format(n))
print('Hello {:<20}!'.format(n))
print('Hello {:^20}!'.format(n))
print('Hello {:=^20}!'.format(n))
print('Hello {:=<20}!'.format(n))
print('Hello {:=>20}!'.format(n))

n1 = 4
n2 = 3
s = n1 + n2
m = n1 * n2
d = n1 / n2
dInt = n1 // n2
e = n1 ** n2

print('The sum is {}, \nmultiplication is {}, \ndivision is {:.3f}, \ndivision with result integer is {}, \nexponentiation is {}'.format(s, m, d, dInt, e))