import datetime
current_date = datetime.datetime.now()
five_days_ago = datetime.datetime(current_date.year, current_date.month, current_date.day - 5, current_date.hour, current_date.minute, current_date.second)

print("Five days ago:", five_days_ago.strftime("%Y-%m-%d"))
