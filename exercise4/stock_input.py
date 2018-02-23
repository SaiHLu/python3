#!/usr/bin/python3

country = input("Where are you from?\n").lower()
stock = input("Which products do you like to order? (iphone, samsung, mi, sony)\n")

iphone = 300000
samsung = 220000
mi = 120000
sony = 340000

if (country == 'myanmar'):
    if stock == 'iphone':
        print('You don\'t need to charge for tax and your price is ({})'.format(iphone))
    elif stock == 'samsung':
        print('You don\'t need to charge for tax and your price is ({})'.format(samsung))
    elif stock == 'mi':
        print('You don\'t need to charge for tax and your price is ({})'.format(mi))
    elif stock == 'sony':
        print('You don\'t need to charge for tax and your price is ({})'.format(sony))
elif (country == 'canada'):
    if stock == 'iphone':
        print('You need to charge for tax and your price is ({})'.format((iphone + (iphone * 0.5))))
    elif stock == 'samsung':
        print('You need to charge for tax and your price is ({})'.format((samsung + (samsung * 0.5))))
    elif stock == 'mi':
        print('You need to charge for tax and your price is ({})'.format((mi + (mi * 0.5))))
    elif stock == 'sony':
        print('You need to charge for tax and your price is ({})'.format((sony + (sony * 0.5))))