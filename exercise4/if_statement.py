#!/usr/bin/python3

favorite_sport = input("What is your favorite sport?\n")
football = "football"

if favorite_sport.lower() == football.lower():
    print("Your favorite sport is {}".format(football))
    print("Go and play " + football)
print("Have a nice day")

deposit = input("Enter your deposit\n")
deposit = int(deposit)

freeToaster = False

if deposit > 100:
    freeToaster = True
elif deposit == 100:
    freeToaster = False
else:
    print("No more toaster")
    exit()

if freeToaster:
    print("Enjoy your free toaster")
else:
    print("You need to pay for your toaster")