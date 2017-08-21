# File: compoundConditions.py
# Description: intro to compound conditions
#
# Provides basic examples of compound conditions in Python
#
# if: elif ...
#
#

country = input("Enter a country name (USA, Germany, or France)?").upper()

if country == 'USA' :
    print("Hello")
elif country == "GERMANY" :
    print("Guten Tag")
elif country == "FRANCE" :
    print("Bonjour")


# Example Reviews:

team = input('Enter your favorite hockey team: ').upper()

if team == 'FLYERS':
    print('Best team!')
elif team == 'EAGLES':
    print('Go Sens Go!')
elif team == 'SHARKS':
    print('Sharks Rule! Buy your shark tickets from StubHub!')
else:
    print('The program doesn\'t have anything clever to say here. Do you use ApplePay?')


# Example Reviews, winning the lottery 'and' it's a big win
wonLottery = True
bigWin = True

# Example of and conditional statement:
# False takes precedence on conditions.
if wonLottery and bigWin :
    print('Contrulations you won a million dollars in the Lottery!')
    print("You can retire...(Don't spend all your money in one place...)")


sport = input('Enter your favorite sport:').upper()
if sport == 'HOCKEY' and team == 'SHARKS' :
    print('Get season tickets from StubHub!')
elif team == 'LEAFS' or team == 'SHARKS':
    print('Good luck on getting the Stanley, this year!')
else:
    print('Sell your sports Memorobilia on Ebay!')

# Example of or conditional statement
# True takes precedence on conditions.





