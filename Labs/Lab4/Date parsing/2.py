import datetime
today = datetime.datetime.now()
yesterday = datetime.datetime(today.year, today.month, today.day - 1)
tomorrow = datetime.datetime(today.year, today.month, today.day + 1)
print("Yesterday:", yesterday.strftime("%Y-%m-%d"))
print("Today:", today.strftime("%Y-%m-%d"))
print("Tomorrow:", tomorrow.strftime("%Y-%m-%d"))