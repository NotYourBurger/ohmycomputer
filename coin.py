import random

import colors_util
def toss():
    players = [0,1]
    first_player= random.choice(players)
    if first_player == 0:
        print(colors_util.yellow("Computer is going to play first"))
        players = [0,1]
    else:
        print(colors_util.yellow("You are going to play first"))
        players = [1,0]

    return players