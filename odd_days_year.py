def is_leap_year(year):
    # Function to check if a year is a leap year
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
def count_odd_days(year):
    # Function to count the odd days for a given year
    # Each non-leap year has 1 odd day, and each leap year has 2 odd days
    odd_days = 1 if not is_leap_year(year) else 2
    return odd_days
def year(y):
    total_days =0
    for yy in range(1, y+1):
        total_days += count_odd_days(yy)
        print(yy,'--->',total_days)
        
    return total_days

print(year(2022)%7)