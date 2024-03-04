import os
os.chdir("Lab6")
file = open("s.txt", encoding='utf-8')
counter = 0
for line in file:
    counter +=1
print(counter)