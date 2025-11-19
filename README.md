# Word Guessing Game

A simple command-line word guessing game. The program picks a secret word
from a `words.txt` file and the player guesses the word one letter at a time.
The player has a limited number of wrong attempts (default: 6).

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Gameplay Example](#gameplay-example)
- [Prepare your word list](#prepare-your-word-list)
- [Contributing](#contributing)
- [License](#license)

## Features

- Single-player CLI game
- Configurable words file and attempts
- Input validation and helpful prompts

## Requirements

- Python 3.6 or newer

## Installation

Clone the repository and (optionally) create a virtual environment:

```bash
git clone https://github.com/rewavestudios/word-guessing-game-cli-py.git
cd word-guessing-game-cli-py
python3 -m venv .venv   # optional
source .venv/bin/activate  # optional
```

There are no external dependencies for the basic game.

## Usage

Run the game from the project directory:

```bash
python3 word_guess.py
```

Options:

- `--words-file, -w`  Path to the words file (default `words.txt`).
- `--attempts, -a`    Number of wrong attempts allowed (default `6`).
- `--debug`           Print the secret word for debugging.

Example with options:

```bash
python3 word_guess.py -w words.txt -a 8 --debug
```

## Gameplay Example

Below is a short, illustrative transcript of one game session (user input
prefixed with `>`):

```
Welcome to the Word Guessing Game!
You have 6 wrong attempts. Good luck!
_ _ _ _ _
Guessed: (none)
Attempts left: 6
Enter a letter (or type "quit"): > a
Wrong guess.
_ _ _ _ _
Guessed: a
Attempts left: 5
Enter a letter (or type "quit"): > e
Good guess!
_ e _ _ _
Guessed: a e
Attempts left: 5
Enter a letter (or type "quit"): > r
Good guess!
r e _ _ _
Guessed: a e r
Attempts left: 5
... (game continues until word guessed or attempts run out)
```

## Prepare your word list

Edit `words.txt` to add one word per line. The loader strips whitespace and
removes non-letter characters, so prefer simple alphabetic words for best
results.

## Contributing

I would love your help! Contribute by forking the repo and opening pull requests. Please ensure that your code passes the existing tests and linting, and write tests to test your changes if applicable.

All pull requests should be submitted to the `main` branch.

## License

See the `LICENSE` file in the repository for license details.
