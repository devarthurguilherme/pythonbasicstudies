money = float(input('How much money do you have?: '))
dolarToday = 5.06

canBuy = money / dolarToday

print('You have {:.2f} BRL, so you can get {:.2f} USD!'.format(money, canBuy))