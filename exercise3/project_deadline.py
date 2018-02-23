#!/usr/bin/python3
import datetime

project_deadline = input("Please enter your project deadline...(dd/mm/YYYY)\n")
project_deadline = datetime.datetime.strptime(project_deadline, "%d/%m/%Y").date()

current_date = datetime.date.today()

day_left = project_deadline - current_date

print("You have ({}) left".format(day_left))

