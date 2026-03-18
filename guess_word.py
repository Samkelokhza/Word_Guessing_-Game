import random

def word_guessing_game():
    """
    A simple word guessing game.
    The computer picks a random word, and the player guesses letters.
    """
    words = ["python", "algorithm", "dragon", "moonlight", "computer"]
    secret_word = random.choice(words)
    guessed_letters = set()
    attempts = 6  # number of wrong guesses allowed

    print("Welcome to the Word Guessing Game!")
    print("Guess the secret word, one letter at a time.")
    print("_ " * len(secret_word))

    while attempts > 0:
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabet letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print("Good guess!")
        else:
            attempts -= 1
            print(f"Wrong guess! Attempts left: {attempts}")

        # Show current progress
        display_word = "".join([letter if letter in guessed_letters else "_" for letter in secret_word])
        print("Word:", display_word)

        if display_word == secret_word:
            print(f"🎉 Congratulations! You guessed the word '{secret_word}'.")
            break
    else:
        print(f"😢 Out of attempts! The word was '{secret_word}'.")

# Run the game
word_guessing_game()