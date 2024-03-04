import time
import math

milliseconds = int(input())
number = int(input())
time.sleep(milliseconds / 1000)
print(f"Square root of {number} after {milliseconds} milliseconds is {math.sqrt(number)}")