#!/usr/bin/python3

user_input = ''

fileName = 'guests.txt'
WRITE = 'w'

guests = open(fileName, WRITE)

while user_input != 'done':
    user_input = input('Enter guest\'s name...(done to exit)\n')
    if user_input == 'done':
        break
    guests.write(user_input + '\n')
guests.close()

print('\n\n')

# Print out written file's data
READ = 'r'
readFile = open(fileName, READ)
fileData = readFile.read()

print(fileData)