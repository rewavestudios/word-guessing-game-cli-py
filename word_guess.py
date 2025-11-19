# Standard library imports
import argparse
import random
import re
import sys
from pathlib import Path


# ---------------------------------------------------------------------------
# File I/O: Read and clean the words file
# This function reads `words.txt`, strips whitespace, lowercases entries and
# removes any non-letter characters so the game only uses alphabetic words.
# ---------------------------------------------------------------------------
def read_words(path: Path):
    try:
        with path.open("r", encoding="utf-8") as fh:
            words = [w.strip().lower() for w in fh if w.strip()]
            # Keep only letters a-z
            cleaned = [re.sub(r'[^a-z]', '', w) for w in words]
            cleaned = [w for w in cleaned if w]
            return cleaned
    except FileNotFoundError:
        print(f'Words file not found: {path}')
        return []


# ---------------------------------------------------------------------------
# Display helper: Render the secret word with guessed letters revealed
# This shows underscores for unknown letters and the actual letter for
# correctly guessed letters. It prints the result with spaces between chars
# for readability.
# ---------------------------------------------------------------------------
def display_word(secret_word: str, guessed_letters: set):
    parts = [c if c in guessed_letters else '_' for c in secret_word]
    # show with spaces for readability
    print(' '.join(parts))


# ---------------------------------------------------------------------------
# Input handling: Prompt the player for a single-letter guess
# Validates input (single a-z character), prevents duplicate guesses and
# supports typing `quit` or `exit` to leave the game.
# ---------------------------------------------------------------------------
def get_guess(guessed_letters: set):
    while True:
        guess = input('Enter a letter (or type "quit"): ').strip().lower()
        if guess in ('quit', 'exit'):
            return None
        if len(guess) != 1:
            print('Please enter exactly one character.')
            continue
        if not re.fullmatch(r'[a-z]', guess):
            print('Please enter a letter a-z.')
            continue
        if guess in guessed_letters:
            print('You already guessed that letter.')
            continue
        return guess


# ---------------------------------------------------------------------------
# Game logic helpers
# - `is_word_guessed` checks whether all letters of the secret word have been
#   revealed by the player's guesses.
# ---------------------------------------------------------------------------
def is_word_guessed(secret_word: str, guessed_letters: set):
    return all(c in guessed_letters for c in secret_word)


# ---------------------------------------------------------------------------
# CLI argument parsing
# Defines available command-line flags for specifying the words file, number
# of allowed wrong attempts, and a debug flag to reveal the chosen word.
# ---------------------------------------------------------------------------
def parse_args():
    p = argparse.ArgumentParser(description='Play the Word Guessing Game')
    p.add_argument('--words-file', '-w', default='words.txt', help='path to words file')
    p.add_argument('--attempts', '-a', type=int, default=6, help='number of wrong attempts allowed')
    p.add_argument('--debug', action='store_true', help='show chosen word for debugging')
    return p.parse_args()


# ---------------------------------------------------------------------------
# Main entrypoint: run the game loop
# Loads words, picks a secret word, then loops prompting the player for input
# until the word is guessed or attempts run out.
# ---------------------------------------------------------------------------
def main():
    args = parse_args()
    path = Path(args.words_file)
    words = read_words(path)
    if not words:
        print('No words loaded. Create a `words.txt` file with one word per line.')
        sys.exit(1)

    secret_word = random.choice(words)
    if args.debug:
        print(f'[DEBUG] secret word: {secret_word}')

    attempts_left = args.attempts
    guessed_letters = set()

    print('Welcome to the Word Guessing Game!')
    print(f'You have {attempts_left} wrong attempts. Good luck!')

    while attempts_left > 0:
        display_word(secret_word, guessed_letters)
        print('Guessed:', ' '.join(sorted(guessed_letters)) if guessed_letters else '(none)')
        print(f'Attempts left: {attempts_left}')

        guess = get_guess(guessed_letters)
        if guess is None:
            print('Goodbye!')
            sys.exit(0)

        guessed_letters.add(guess)

        if guess in secret_word:
            print('Good guess!')
            if is_word_guessed(secret_word, guessed_letters):
                display_word(secret_word, guessed_letters)
                print('Congratulations! You guessed the word!')
                sys.exit(0)
        else:
            print('Wrong guess.')
            attempts_left -= 1

    # out of attempts
    print(f'Game over! The word was: {secret_word}')
    sys.exit(0)


if __name__ == '__main__':
    main()
