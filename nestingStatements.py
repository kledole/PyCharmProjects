# File: nestingStatements.py
# Description: Examples showing nesting in statements
#
# Timestamp: 5:47:22

monday = True
freshCoffee = True

if monday :
    # Add code here to check if the coffee is fresh...
    if freshCoffee :
        print("Fresh coffee exists! Caffeinate up!")

    # If statement is nested (indented), it will only execute
    # if it is monday.

    if not freshCoffee :
        print("go buy a coffee!")
    print("Kick it in gear, dude!  It\'s Monday Morning....")
print("now you can start work.")
