# File: dateTimes.py
# programs with datetime examples

# uses: datetime

import datetime
currentDate = datetime.datetime.now()

print(currentDate.minute)

print(currentDate)
print(currentDate.month)
print(currentDate.year)

print(currentDate.strftime('%d %b, %Y'))
print(currentDate.strftime('%d %b %y'))


