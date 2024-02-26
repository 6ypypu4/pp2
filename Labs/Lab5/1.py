import re
import io
file = io.open("row.txt", encoding='utf-8')

for line in file:
    x = re.findall("ab*", line)
    print (x)