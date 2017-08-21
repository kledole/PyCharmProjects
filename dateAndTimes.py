# File: dateAndTimes.py
# Description: Excercises to learn date and time format
#
# The import statement gives us access to
# the functionality of the datetime class
# - import datetime
# today() is a function that returns today's date:
# - today()
#  Example: print(datetime.date.today())

# Tip: Also learned pyCharm 'power save mode' disables
# the context sensitive help!
# If disabled see: File -> PowerSaveMode

# Tip: (un)comment blocks of code in Pycharm: (select) %/

# Formatting Dates:
# References:
# %b is the month
# %B is the full month name
# %y is the two digit year
# %a is the abbreviated day of the week
# %A is the day of the week

# For a full  list visit strftime.org

#  Exercise:
# print the date in the following format:
# "Please attend our event Sunday, July 20 in the year 1997"



import datetime

# currentDate = datetime.date.today()
# print('Today\'s date is: ', currentDate )
# print('Day: ', currentDate.day)
# print('Year: ', currentDate.year)
# print('Month: ', currentDate.month)
#
# print('This is a different format of the date.')
# print(currentDate.strftime('%b %d, %Y'))
#
# # Format Exercise: Time: 3:39:26 / 11:11:04
# print(currentDate.strftime
#       ('Please attend our event %A, %B %d in the year %Y. '))

currentDate = datetime.datetime.today().date()


birthday = input('Please enter a birthday. (mo/dd/yyyy)')
birthdate = datetime.datetime.strptime(birthday, '%m/%d/%Y').date()
print(birthday)

days = abs(birthdate - currentDate)
print(days.days, ' days exist between: Today and the birthday.')

