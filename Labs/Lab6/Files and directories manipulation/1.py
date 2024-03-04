import os

s = os.getcwd()

#ALL:
print(os.listdir(s))


for n in os.listdir(s):
    if os.path.isfile(os.path.join(s, n)):
        print("File:", n)
    elif os.path.isdir(os.path.join(s, n)):
        print("Directory:", n)