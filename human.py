import random
import input_util

import colors_util

def play_human(repeat, low, high):
    number = random.randint(low,high)
    result = False
    
    for _ in range(repeat):

        guess = input_util.read_int(colors_util.green(f'Guess the number between {low}-{high}:'), low, high)
        if guess < number:
             print(colors_util.yellow("Your guess is lower than the number"))
        elif guess > number:
            print(colors_util.yellow("Your Guess is higher than the number"))
        else:
            print(colors_util.green("You guessed the right number"))
            result = True
            break
    if not result:
        print(colors_util.yellow(f"The Number Was: {number}"))
    
    return result