# Lesson 2
# Moving along!...
# Program: Module2DisplayingText
# Description: practice/review - will demonstrate use of quotes
# and the print statement
#
# Finally: print out the challenge poem
# There once was a move star icon
# who preferred to sleep with the light on
# They learned how to code
# a device that sure glowed
# and lit up the night using Python!

#: Time: 55:36
print('The caybara is the worlds largest rodent')
print('The capybara likes to live in groups')
print("The capybara likes to swim")
print('This is a double quote ".', "This is a single quote: '.")
print('This is a double quote ".' +  "This is a single quote: '.")

print(""" The capybara lives in \nSouth America""")
print(""" This is the strangest way
to print over multiple lines, why not use \\n?""")

print('Here is a double quote " and here is a single quote \'')

print('Here is a doublebackslash: \\')

# The following sets of comments have mistakes.
# Missing quotes:
# print(Hickory Dickory Dock)
# Actual error: IndentationError: unexpected indent

# Missing control character for single quote in string
# print('It's a small world')
# Error:
#print('It's a small world')
    #^
#IndentationError: unexpected indent

# Mixed quotes
#print("Hi there')
#Error:
#    print("Hi there')
#                    ^
#SyntaxError: EOL while scanning string literal


# print command syntax error, 'prnit'(misspelling)
#prnit("Hello World!")

# Error:
# NameError: name 'prnit' is not defined

# The following lines of code correct the issues.
# Corrections:
print('Hickory Dickory Dock')
print('It\'s a small world')
print("Hi there")
print("Hello World")

# Print out the poem:
print('\n' * 5)
print('There once was a move star icon')
print('who preferred to sleep with the light on')
print('They learned how to code')
print('a device that sure glowed')
print('and lit up the night using Python!')
