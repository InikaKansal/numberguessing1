import random
number= random.randint(1,10)
chances = 0
while chances < 5:
    chances = chances + 1
    guess = int(input("Enter a number"))
    if number > guess:
        print("Too Low! Guess Higher")
    elif number < guess:
        print("Too High! Guess Lower")
    elif number == guess:
        print("You Won!")
        break
            
if chances >= 5:
    print("You Lose!")
    print("The number was " + str(number))