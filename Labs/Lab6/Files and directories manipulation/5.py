import os
os.chdir("Lab6")
data = ['banana','orange']
with open("mylist.txt", 'w') as file:
    for item in data:
        file.write(str(item) + '\n')