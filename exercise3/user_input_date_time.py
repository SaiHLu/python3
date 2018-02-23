#!/usr/bin/python3
import datetime

birthday = input("What is your birthday? (mm/dd/YYYY)")

# birthday = datetime.datetime.strptime(birthday, '%m/%d/%Y')
nextBirthday = datetime.datetime.strptime(birthday, '%m/%d/%Y').date()

print("Your birthday is ", birthday)

# convert string to datetime strptime(userInput, format)


# Days Remain Before Your Next Birthday Will Come
currentDate = datetime.date.today()

dayLeft = nextBirthday - currentDate
print(dayLeft)

# Get Time (Hour:Minute:Second)
currentTime = datetime.datetime.now()
print("Hour: ", currentTime.hour)
print("Minute: ", currentTime.minute)
print("Second: ", currentTime.second)


# %H is hour
# %m is minute
# %s is second
