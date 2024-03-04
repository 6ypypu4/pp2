import os
'''
print(os.getcwd()) #текущая дириктория 
#os.chdir('..') #вход в предыдущую в дирикторию
#os.chdir('Labs') #вход в предыдущую в дирикторию
os.chdir('Lab6') #вход в дирикторию
#os.mkdir("folder") #создание новой папки
s = os.path.isdir("Folder") # проверка существования папки
print(s)
s = os.path.isfile("File")#проверка существования файла
print(s)
file = open("text.txt", "w")
file.write("КАПЕЦ ТРЯХАНУЛО \n pobeda")
file.close()
os.rename("text.txt", "earthquake.txt")'''
os.chdir('Lab6') #вход в дирикторию
print(os.listdir())