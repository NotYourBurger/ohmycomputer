# Oh My Computer

A two-player number guessing game for the terminal: you against the computer, first to 6 points.

Written in Python with no dependencies, standard library only.

## How to play

```bash
python main.py
```

A coin toss decides who goes first, then turns alternate:

- **Your turn.** The computer picks a secret number between 1 and 10. You get 3 guesses, and it tells you whether each guess was too high or too low.
- **Computer's turn.** You think of a number between 1 and 10 and type it in. The computer gets 3 guesses at it.

Guess right and you score a point. The first player to reach 6 points wins, and the game ends the moment someone gets there, so winning the toss is a real advantage.

## Project structure

| File | What it does |
|---|---|
| `main.py` | Entry point. Sets the rules (target 6, 3 guesses, range 1 to 10) and announces the winner |
| `number_game.py` | The game loop. Alternates turns, tracks score, ends the game at the target |
| `human.py` | Your turn: picks a secret and gives higher/lower hints |
| `computer.py` | The computer's turn: its guessing algorithm |
| `coin.py` | The opening coin toss |
| `input_util.py` | Reads an integer and re-asks until it is valid and in range |
| `colors_util.py` | ANSI escape codes for colored terminal output |

## How the computer guesses

The computer uses binary search with jitter:

```python
guess = max(low, min(high, (low + high) // 2 + random.randint(-1, 1)))
```

It guesses near the middle of whatever range is still possible, then narrows that range using its own hint. If 5 was too low, everything below 6 is ruled out. Halving the range each time is much stronger than guessing randomly.

The `random.randint(-1, 1)` nudges the guess by up to one either way. Without it the computer is perfectly predictable. It would always open on 5, and a player who knew that could always pick a number it cannot reach in 3 guesses. The `max` and `min` clamp keeps the jittered guess inside the valid range, so it never wastes a turn on a number it has already ruled out.

## What I learned

- Binary search, and why halving a range beats guessing
- Keeping each piece in its own module instead of one long file
- Validating user input so bad typing cannot crash the program
- That a small rule change (3 guesses vs 4) can completely change how a game feels
