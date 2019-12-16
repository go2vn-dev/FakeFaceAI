import random

cont = True

while cont:
    print("Guess the number: ...")
    randNum = random.randint(0,6)
    answer = input("your number is ")
    if str(randNum) == answer:
        print("You won !!!")
        break
    else:
        print("Guess Again")
        print("Random number is " + str(randNum))
        print()

