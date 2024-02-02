import random
def guess_the_number():
    print("Hello! What is your name?")
    name = input()
    txt = "Well, {}, I am thinking of a number between 1 and 20."
    print(txt.format(name))
    number = random.randint(1, 20)
    tries = 1
    print("Take a guess.")
    urnam = int(input())
    while urnam != number:
        if tries != 0:
            if urnam > number:
                print("Your guess is too high.")
            elif urnam <number:
                print("Your guess is too low.")
        tries = tries + 1
        urnam = int(input())
    txt = "Good job, {}! You guessed my number in {} guesses!"
    print(txt.format(name,tries))

guess_the_number()
