"""
P
Given a year, return the number of Friday the 13ths in that year

E
- using the Gregorian calendar

D
input: integer
output: integer

A
- Iterate over all months of the given year
- For each month, get day that falls on the 13th
- count the 13ths that fall on a Fri
- return count

"""
from datetime import date

def friday_the_13ths(year):
    counter = 0
    for month in range(1, 13):
        if date(year, month, 13).weekday() == 4:
            counter += 1

    return counter

print(friday_the_13ths(1986) == 1)      # True
print(friday_the_13ths(2015) == 3)      # True
print(friday_the_13ths(2017) == 2)      # True