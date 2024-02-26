import re
import io
file = io.open("row.txt", encoding='utf-8')
def camel_to_snake(camel):
    snake = ''
    for char in camel:
        if char.isupper():
            snake += '_' + char.lower()
        else:
            snake += char
    return snake

for line in file:
    x = camel_to_snake(line)
    print (x)
