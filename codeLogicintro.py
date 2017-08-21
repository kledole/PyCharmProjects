# File: codeLogicintro.py
#
# Basics to conditional logic.
##
# Time: 4:10:28

# Review of conditionals:
# ==   is equal to
# !=   is not equal to
# < is less than
# < is greater than
# >= is greater than or equal to
# <= is less than or equal to
# Tip review for PyCharm %/... comment blocks of code...

# Note usage of the ':' character at end of conditions.
# Note: simplified use of indentation, endifs and ends not required.
# Use of upper(), or lower() functions for comparisons

# Booleans are case sensitive: True and False



# Case 1:

answer = input("Would you like express shipping? (Type yes or no)")
if answer.upper == "YES" :
    print("That will be an extra $10")
    print("Suprise! Because you selected yes, you'll get free express shipping!")
else:
    print("Surprise!  Standard shipping is only 2$, you saved 8 dollars!")
print("Have a nice day")

# Case 2:
# if conditions with numbers
# intro to boolean conditions (variable: freebonus)
#           - boolean is case sensitive: True or False
#    Remember to convert numeric input values to numeric types.
#

freebonus = False

deposit = float(input("How much do you want to deposit? "))
if deposit > 100:
    print("Enjoy your toaster!")
    if deposit >= 10000:
        freebonus = True
else:
    print("Enjoy your free mug!")
print("Have a nice day!")

if freebonus :
    print("Thank you your interest rate is now 20%!")
    print("Feel free to deposit more money for us to loan.")


# Case3 - Exercise:
# Calculate shipping charge for a shopper
# Ask the user to enter the amount of the shipment
# If the total is under $50 add $10, otherwise shipping is free.
# Inform the user of the total shipping cost.
# Test the program for values > 50, < 50, and equal to 50.

cost = input('Please enter the amount for your product: ')
print("Calculating shipment prices...")

cost = float(cost)

shipping = float(0)

if cost < 50 :
    shipping = float(10)
    print('Additional ${0:.2f} added for shipping....'.format(shipping))

total = cost + shipping

print('Your total cost w/ shipping is ${0:.2f} .'.format(total))





