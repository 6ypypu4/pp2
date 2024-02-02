import random
def guess_the_number_ver2():
    print("This is a game that test your luck and memory")
    print("I'll come up with a sequence of numbers from 1 to N. \nYou need to guess its sequence, preferably without errors. \nNumber N is the difficulty, you can choose it yourself \nIf you forger a previous numbers type '0'(not recomended)")
    n = int(input("\nChoose the dificullty (int number>1) : " ))
    while n < 2:
       n = int(input("Did i not ask to choose int number>1?\n" ))
    m = n + 1
    numbers = []
    for i in range(1,m):
        numbers.append(i)
    tries = 0
    while n > 0:
        number = numbers[random.randint(0, n-1)]
        print("Take a guess.")
        urnam = 0
        while urnam != number:
            if urnam != 0:
                if urnam > number:
                    print("Your guess is too high.")
                    tries = tries + 1
                elif urnam <number:
                    print("Your guess is too low.")
                    tries = tries + 1
            urnam = int(input())
            if urnam == 0:
                print(numbers)
        n = n - 1
        numbers.remove(number)
        if n > 0: 
            print("Well done! Now let's start round " + str(m - n))
    txt = "Good job! You guessed all {} numbers only by {} mistakes"
    print(txt.format(m - 1, tries))
    
guess_the_number_ver2()
a = input()