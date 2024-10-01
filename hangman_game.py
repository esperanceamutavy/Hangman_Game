import random
import string

from words import words


def get_valid_word(words):
    word = random.choice(words)  # randomly choose a word from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed

    lives = 6  # user lives

    # while the word has not been guessed and the user has lives
    while len(word_letters) > 0 and lives > 0:
        # letters used
        print(f"You have {lives} lives left and you have used these letters: ", ' '.join(used_letters))

        # what the current word is (e.g. W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input("Enter a letter: ").upper()

        # if the user types in a valid letter
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print("Good guess!")
            else:
                lives -= 1
                print(f"{user_letter} is not in the word.")

        elif user_letter in used_letters:
            print("You have already guessed that letter. Try again.")

        else:
            print("Invalid letter. Try again.")

    # if the player runs out of lives
    if lives == 0:
        print(f"You lost! The correct word was {word}.")
    else:
        print(f"Congratulations! You guessed the word {word} correctly!")

# Start the game
hangman()
