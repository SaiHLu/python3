#!/usr/bin/python3
import sys

firstNumber = float(input('Enter first number.\n'))
secondNumber = float(input('Enter second number.\n'))

try:
    result = firstNumber / secondNumber
    print(result)
except ZeroDivisionError as error:
    print(error)
    sys.exit()
except:
    errors = sys.exc_info()[0]
    print(errors)
# finally:
#     print('I will always run either it is true or false')
print('I will not run if you use sys.exit()')