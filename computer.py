import random
import input_util

import colors_util


def play_computer(repeat, low, high):
    
    number = input_util.read_int(colors_util.yellow(f'Think of a Number between {low} - {high}: '), low, high)
       
    result = False
    for _ in range(repeat):
        
        guess = max(low, min(high, (low + high) // 2 + random.randint(-1, 1)))
        print(colors_util.red(f"My guess is: {guess}"))
        if guess < number:
            
            print(colors_util.red(f"Dang! {guess} was too low"))
            low = guess +1 
        elif guess > number:
            print(colors_util.red(f"Ohh Shoot, {guess} was too high"))
            high = guess -1
        
        else:
            print (colors_util.red(f"I knew I was Right about {guess}"))
            
            result = True
            break
    return result