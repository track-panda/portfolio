import random

def word_choice():
    """Gets random word from a list."""
    word_options = ['Turtles','Hyperbole','Lacey','Emerson','Homework','Physiology']
    return random.choice(word_options)

def lets_play_hangman():
    """Plays the Hangman game."""

    word = word_choice()
    word_letters = set(word.lower())  # Ensure word is in lowercase
    alphabet = set(chr(x) for x in range(97,123))  # Set of lowercase letters
    letters_guessed = set()

    lives = 5

    while len(word_letters) > 0 and lives > 0:
        print("You have guessed the following letter(s):","".join(letters_guessed))

        word_list = [letter if letter in letters_guessed else '_' for letter in word]
        print("Current word: ","".join(word_list))

        user_letter = input("Please guess a letter:").lower()

        # Ensure valid input (a single alphabetical character)
        if len(user_letter) != 1 or user_letter not in alphabet:
            print("Invalid input. Please enter a single letter.")
            continue

        if user_letter in letters_guessed:
            print("You have already guessed this letter. Please try again.")
        else:
            letters_guessed.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
                print("What an unlucky guess!")

    if lives == 0:
        print("You died. What a shame. The word was:", word)
    else:
        print("You have guessed the word", word, "!!")

lets_play_hangman()
