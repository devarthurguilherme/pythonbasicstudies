productPrice = float(input('Digit product value: '))
discount = productPrice * 0.05
newPrice = productPrice - discount

print('Now, the product is {:.2f} dollars'.format(newPrice))