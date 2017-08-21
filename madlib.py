# File: madlib.py
# Description: simple input/print program
# prompts user for input
# outputs a madlib story

#
#
print('The following will print a story.')

name = input('What is your name? ')
hobby = input('What is your favorite hobby? ')
color = input('What is your favorite color? ')
location = input('Where would you like to go on vacation? ')
adjective = input('Type in an adjective: ')
adverb = input('Type in an adverb: ')
sound = input('Type in an exclamation: ')
feeling = input('Type in a feeling: ')

print('\n' * 5)
print('The famous story of ' + name + ' in ' + location + '.' )

print('Once upon a time, in ' + location )
print('a character named ' + name + ' travelled to ' + location)

print(name + ' noticed a ' + color + ' boat ')
print('sitting on the ground, and '+ adverb + ' climbed aboard.' )
print('Feeling ' + feeling + ', ' + name + ' screamed ' + sound + '!!!!')
print('and began to ' + hobby)
print('\n to be continued...\n')


