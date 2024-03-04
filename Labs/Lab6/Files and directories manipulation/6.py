import os
os.chdir("Lab6")
for i in range(26):
        letter = chr(ord('A') + i)
        filename = letter + ".txt"
        file = open(filename, 'w')