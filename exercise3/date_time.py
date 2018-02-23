#!/usr/bin/python3
import datetime

currentDate = datetime.date.today()
print(currentDate.day)
print(currentDate.month)
print(currentDate.year)
print(currentDate)
print(currentDate.strftime('%d %b %Y'))

# %b is the month abbreviation
# %B is the full month name
# %y is two digit year
# %a is the day of the week abbreviated
# %A is the day of the week
# full list at => strftime.org
# change particular language using python => http://babel.pocoo.org/

print(currentDate.strftime("Please attend my event in %A, %B %d %Y"))