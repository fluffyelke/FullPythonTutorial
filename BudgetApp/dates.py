import datetime

curr_day = datetime.datetime.now().day
curr_month = datetime.datetime.now().month
curr_year = datetime.datetime.now().year

print(curr_day)
print(curr_month)
print(curr_year)


current_month = datetime.datetime.now().strftime('%m') # 02 This is 0 padded
current_month_text = datetime.datetime.now().strftime('%h') # Feb
current_month_text_2 = datetime.datetime.now().strftime('%B') # February

current_day = datetime.datetime.now().strftime('%d')   # 23 This is also padded
current_day_text = datetime.datetime.now().strftime('%a')  # Fri
current_day_full_text = datetime.datetime.now().strftime('%A')  # Friday
print(current_month)
print(current_month_text)
print(current_month_text_2)
print(current_day)
print(current_day_text)
print(current_day_full_text)