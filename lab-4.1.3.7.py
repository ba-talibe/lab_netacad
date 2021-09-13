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
    
        

testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")