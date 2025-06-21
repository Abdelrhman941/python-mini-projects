import calendar
from datetime import datetime

year  = int(input("Enter year: "))
month = int(input("Enter month: "))

cal = calendar.month(year, month)
print("----------------------------------")
print(cal)
print("----------------------------------")
now = datetime.now()
current_day = now.day
print(f"Today >>>> {current_day}.")
