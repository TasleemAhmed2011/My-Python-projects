'''from  datetime import date,time,datetime
now = datetime.now()
current_date = date.today()
current_time = time.now()
print("Current date:", current_date)
print("Current time:", current_time)
print("Current datetime:", now)
print()'''

import random
import time
def get_random_date(start_date, end_date):
 print("Generating a random date between", start_date, "and", end_date)
print()

import calendar
year=input("Enter the year: ")
for month in range(1, 13):
    name = calendar.month_name[month]
    print(name, year)
