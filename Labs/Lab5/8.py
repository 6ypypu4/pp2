import re
import io
file = io.open("row.txt", encoding='utf-8')

for line in file:
    x = re.split('(?=[A-Z])', line)
    print (x)