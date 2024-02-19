from datetime import datetime
def date_difference(date1, date2):
    timestamp1 = datetime.timestamp(date1)
    timestamp2 = datetime.timestamp(date2)

    difference_in_seconds = abs(int(timestamp1 - timestamp2))
    return difference_in_seconds
#YYYY-MM-DD HH:MM:SS
date_str1 = input()
date_str2 = input()

date1 = datetime.strptime(date_str1, "%Y-%m-%d %H:%M:%S")
date2 = datetime.strptime(date_str2, "%Y-%m-%d %H:%M:%S")

difference_seconds = date_difference(date1, date2)
print( difference_seconds)
