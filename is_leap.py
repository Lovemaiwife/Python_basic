def is_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0 and year % 3200 != 0):
        return True
    else:
        return False
year = int(input('please enter the year: '))
print(is_leap(year))