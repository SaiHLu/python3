#!/usr/bin/python3
area = 0
width = input("Please enter the width...\n")
height = input("Please enter the height...\n")

# int() float() long() str()

area = (float(width) * float(height)) / 2

print("The are is %.2f" % area)
# print("The are is %03d" %area) 00area
# print("The are is %f" %area) area.00000
# print("The are is %.2f" %area) area.00

print("The area is {0:d}. The second argument is {1:.2f} and the third is {2:03d}".format(int(area), area, int(area)))
