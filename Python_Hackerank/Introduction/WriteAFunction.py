def is_leap(year):
    ischeck = year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
    return ischeck

year = int(input())