#!/usr/bin/python3
name = input("What is your name?\n")
print("Welcome ..", name)

# name = 'sai sai'
# print("Updated name to ... ",name)

# lower() upper() swapcase()
# find() count() capatilize() replace()

country = input("Where are you from?\n")
country = country.upper()
print("Your name is " + name + ". You live in " + country)

hello = "Hello world"
print(hello.find('o'))
print(hello.count('ld'))
print(hello.capitalize())
print(hello.replace('world', 'World'))