# Program: Module3
# Description: Exercises for input and variable assignments
# Introduction to:
# input() - function to prompt user for input
# print() - review of print function


#
# Variable assignments
# Variables in Python can not contain spaces
#           Are case sensitive.  Treat everything as case-sensitive
#           Can not start with a number.
#           Should be descriptive, but not too long.
#           Use a casing Scheme.  ie: camelCasing or PascalCasing
#

# Sample: Exercise Valid and invalid variables:
# Variable1 - non-descriptive, (not recommended)
# First Name (space, invalid)
# Date (reserved word, non-descript)
# 3Name (begins with number, invalid)
#
# DOB - confusing/ acronym if known, ok (context)
# DateOfBirth - ok
# YourFavoriteSignInTheHoroscope - ok, but too long?





# Prompt user for their name:
name = input("What is your name? ")
# print out the name (input by the user)
print(name)
# Re-assign the variable 'name'
name = "Mary"
# print out the new assignment of the name
print(name)

# Update the name again
name = 'Snoopy'
print(name)

firstName = input('What is your First Name? ')
lastName = input('What is your Last Name? ')
print("hello " + firstName + ' ' + lastName)

message = 'Hello world'
print(message)
print(message.lower())
print(message.upper())
print(message.swapcase())


country = input('What country does ' + name + ' live in? ' )
country = country.upper()
print('Hello, ' + name + ' lives in ' + country)

# Section
# Demonstration of simple functions and utilization of
# UI features

message = 'hello world'
print(message.find('world'))
print(message.count('o'))
print(message.capitalize())
print(message.replace('Hello', 'Hi'))

