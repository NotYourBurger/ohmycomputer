from number_game import play_game
import colors_util
def main():
    computer_score , player_score = play_game(6, 3, 1, 10)
    if player_score > computer_score:
        print (colors_util.green(f"You Win with {player_score} Score"))
        print (colors_util.red(f"Computer Lost With {computer_score}"))
    elif computer_score > player_score:
        print (colors_util.red(f"Computer Won with {computer_score} Score"))
        print (colors_util.red(f"You Lost with {player_score} Score"))
    else:
        print(colors_util.yellow("You both scored the same! Tie"))
if __name__ == "__main__": main()