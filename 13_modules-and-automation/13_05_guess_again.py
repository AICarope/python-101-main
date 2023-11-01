# Re-create the guess-my-number game from scratch. Don't peek!
# This time, give your players only a certain amount of tries 
# before they lose.

import random

num = random.randint(1,5)
guess = None

while guess != num:
    guess = input("try a number btw 1 to 5:")
    guess = int(guess)

    if guess == num:
        print('yes')
        break
    else:
        print('nope')
        