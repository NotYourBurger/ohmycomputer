import coin
import computer
import itertools
import human
import colors_util

def play_game(target,loops, low, high):
    computer_score = 0
    player_score = 0
    
    

    for current_player in itertools.cycle(coin.toss()):
        if current_player == 0:

            computer_result= computer.play_computer(loops, low, high)
            
            if computer_result: 
                computer_score += 1
                print(colors_util.yellow(f"Computer Score: {computer_score}"))
            else:
                print(colors_util.red("Computer lost"))
                
        else:
            
            human_result= human.play_human(loops, low, high)
            if human_result:
                player_score += 1
                print(colors_util.yellow(f"Your Score is: {player_score}" ))
            else:
                print(colors_util.red("You lost"))
        if computer_score == target or player_score ==target:
            break

    return computer_score, player_score

