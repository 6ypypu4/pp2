'''
let x = num of chikens, y = nums of rabbits
a = heads b = legs
{x+y = a    {x + y = a    {y = (b - 2a)/2
{2x+4y = b  {2y = b - 2a  {x = a - (b - 2a)/2
 
'''
def classic_puzzle(numheads, numlegs):
    print("there are", int((numlegs - 2*numheads)/2), "rabbits" )
    print("there are", int(numheads -(numlegs - 2*numheads)/2), "chikens" )
 
a=35
b=94
classic_puzzle(a, b)