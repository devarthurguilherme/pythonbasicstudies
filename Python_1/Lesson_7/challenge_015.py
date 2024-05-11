d = int(input("How many days were you with car? : "))
km = float(input("How many kilometers did you do? : "))
mustPay = (d * 60) + (km * 0.150)

print('You must pay {:.2f} dollars!'.format(mustPay))