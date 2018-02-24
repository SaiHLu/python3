#!/usr/bin/python3

guests = []
guest = ''

while guest != 'done':
    guest = input("Enter guest's name. (done to exit)\n")
    if guest == 'done':
        print('\n\n')
        break
    guests.append(guest)

guests.sort()
for currentGuest in guests:
    print(currentGuest)