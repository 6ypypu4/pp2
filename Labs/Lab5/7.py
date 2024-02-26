import re
import io
file = io.open("row.txt", encoding='utf-8')
def snake_to_camel(snake):
    camel = ''
    nextone = False
    for char in snake:
        if char == '_':
            nextone = True
        elif nextone == True:
            camel += char.upper()
            nextone = False
        else:
            camel += char
    return camel

for line in file:
    x = snake_to_camel(line)
    print (x)
