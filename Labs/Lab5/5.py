import re
import io
file = io.open("row.txt", encoding='utf-8')

for line in file:
    x = re.findall("a[a-z]*b", line)
    print (x)