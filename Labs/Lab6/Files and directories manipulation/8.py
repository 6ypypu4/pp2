import os

path = input()
if not os.path.exists(path):
    print("File not found:", path)

if not os.access(path, os.W_OK):
    print("No write access to the file:", path)
try:
    os.remove(path)
    print("File deleted successfully:", path)
except:
    pass

