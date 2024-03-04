string = "Hello World"

upper= sum(1 for char in string if char.isupper())
lower = sum(1 for char in string if char.islower())
print("Number of uppercase letters:", upper)
print("Number of lowercase letters:", lower)