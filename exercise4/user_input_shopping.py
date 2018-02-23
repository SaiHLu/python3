#!/usr/bin/python3

charge = input("Please enter your total charges\n")
charge = int(charge)

freeCustom = False

if charge <= 50:
    charge += 10
    freeCustom = False
else:
    freeCustom = True

if freeCustom: 
    print("Enjoy your free charge")
else:
    print("You need to charge ${0:3d}".format(charge))