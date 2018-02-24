#!/usr/bin/python3

fileName = 'demo.txt'
WRITE = 'w'
APPEND = 'a'
READ = 'r'
READWRITE = 'w+'

# files = open(fileName, mode=READ)
# print(files.read())
# files.close()

# files = open(fileName, mode=APPEND)
# files.write('I am new two\n')
# files.write('sorry about that')
# files.close()

files = open(fileName, mode=WRITE)
user_input = ''
while user_input != 'exit':
    user_input = input('Enter some data....(type exit to exit)')
    if user_input == 'exit':
        break
    files.write(user_input + '\n')
files.close()


print('Operation success')