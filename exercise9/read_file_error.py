#!/usr/bin/python3
import sys

user_input_file_name = input('Enter file name you want to read.\n')

try:
    files = open(user_input_file_name, mode='r')
    data = files.read()
    print(data)
except FileNotFoundError as error:
    print(error)
except:
    errors = sys.exc_info()
    print(errors)

def otherFileWillCallMeToExecute():
    print("I came from read_file.py")