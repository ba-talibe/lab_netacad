def isYearLeap(year):
    if (year%400 == 0) or (year%4 == 0 and year%100 != 0):
        return True
    else:
        return False

#
# your code from LAB 4.1.3.6
#

def daysInMonth(year, month):
    monthlen = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    #
    # put your new code here
    if month == 2:
        if isYearLeap(year):
            return 29
        else:
            return 28
    else:
        return monthlen[month - 1]


#
# your code from LAB 4.1.3.7
#

def dayOfYear(year, month, day):
    days = 0
    for i in range(1, month):
        days += daysInMonth(year, i)
    
    days += day
    return days

print(dayOfYear(2010, 12, 31))