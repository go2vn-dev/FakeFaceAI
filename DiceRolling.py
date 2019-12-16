import random

cont = True

while cont:
    print("Dice is rolling...")
    num = random.randint(0, 6)
    print("Number is: " + str(num))
    answer = input("Continue to Roll (Y/N) ?")
    if answer == 'N' or answer == 'n':
        print("Program Ended.")
        break



