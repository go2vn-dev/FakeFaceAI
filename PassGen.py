import string
import random

lowerCase = string.ascii_lowercase
upperCase = string.ascii_uppercase
digit = string.digits
squence = lowerCase + upperCase + digit

cont = True

def pass_gen(opt, size):
    if opt == 'easy':
        size = 3
        return ''.join(random.sample(squence, size))

    if opt == 'hard':
        return ''.join(random.sample(squence, size))

    if opt == 'end':
        return 'Program ends'
while cont:
    option = input("hard or easy password ? ")
    print(pass_gen(option, 9))
    if option == 'end':
        break
