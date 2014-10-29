def isLeapYear(year):
    if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
        return True
    else:
        return False


def days(year, month):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    if month in [4, 6, 9, 11]:
        return 30
    if month == 2:
        if isLeapYear(year):
            return 29
        else:
            return 28

total_days = 1  # Monday
total_days += 365  # 1900
count = 0
for y in xrange(1901, 2001):
    for m in xrange(1, 13):
        if total_days % 7 == 0:  # Sunday
            count += 1
        total_days += days(y, m)
print count
