#!/usr/bin/python3
import csv

fileName = 'demo.txt'
WRITE = 'w'
APPEND = 'a'
READ = 'r'
READWRITE = 'w+'

# files = open(fileName, mode=READ)
# print(files.read())
# files.close()

# Read file line by line
# files = open(fileName, mode=READ)
# print(files.readline())
# files.close()

# Read file line by line using csv
with open(fileName, mode=READ) as data:
    allData = csv.reader(data)

    for currentRow in allData:
        print(':'.join(currentRow))
        # for currentWord in currentRow:
        #     print(currentWord)