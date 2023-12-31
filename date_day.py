#read date and find the day like 24/07/2024 : Monday 

# l=list((input("Enter the date  dd/mm/yyyy :").split("/")))
# print(l)

# months={"01":3,"03":3,"04":2,"05":3,"06":2,"07":3,"08":3,"09":2,"10":3,"11":2,"12":3,}


'''

def find_day_of_week(day, month, year):
    if month < 3:
        month += 12
        year -= 1

    K = year % 100
    J = year // 100

    # Zeller's Congruence formula
    day_of_week = (day + (13 * (month + 1)) // 5 + K + K // 4 + J // 4 + 5 * J) % 7

    # Mapping the result to the corresponding day of the week
    days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    return days[day_of_week]

# Example usage:
date = input("Enter the date in the format (dd/mm/yyyy): ")
day, month, year = map(int, date.split('/'))
day_of_week = find_day_of_week(day, month, year)
print(f"The day of the week for {date} is {day_of_week}.")
'''


def is_leap_year(year):
    # Function to check if a year is a leap year
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def count_odd_days(year):
    # Function to count the odd days for a given year
    # Each non-leap year has 1 odd day, and each leap year has 2 odd days
    odd_days = 1 if not is_leap_year(year) else 2
    return odd_days

def get_days_in_month(month, year):
    # Function to get the number of days in a given month
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and is_leap_year(year):
        return 29
    return days_in_month[month]

def count_days_since_1st_Jan_1AD(day, month, year):
    # Function to count the total number of days from 1st January 1 AD to the input date
    total_days = 0

    # Years from 1 AD to the input year (excluding the input year)
    for y in range(1, year):
        total_days += count_odd_days(y)

    # Months from January to the input month (excluding the input month)
    for m in range(1, month):
        total_days += get_days_in_month(m, year)

    total_days += day  # Days from 1st of the input month to the input day (we don't subtract 1 here)

    return total_days

def find_day_of_week(day, month, year):
    # Calculate the day of the week using 1st January 1 AD as the reference date
    days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    total_days = count_days_since_1st_Jan_1AD(day, month, year) % 7
    return days_of_week[total_days]

# Example usage:
date = input("Enter the date in the format (dd/mm/yyyy): ")
day, month, year = map(int, date.split('/'))
day_of_week = find_day_of_week(day, month, year)
print(f"The day of the week for {date} is {day_of_week}.")





