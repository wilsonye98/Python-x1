# You are given a date. Your task is to find what the day is on that date.

import calendar

def find_weekday(string):
    month, day, year = string.split(' ')
    weekday = calendar.weekday(int(year), int(month), int(day))
    weekday_str = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    fweekday = [x for i,x in enumerate(weekday_str) if i == weekday]
    return fweekday[0]

print(find_weekday('08 05 2015'))