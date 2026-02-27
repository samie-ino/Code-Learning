import random
import string


# Wordbank of Understanding
# words: This is the list of words we are using
# random_words: This is the random words that will be chosen there is no special order in hangman
# add_length: This is needed to know the amount of spaces needed for each random word
# word_length: This is the length of the word that is random
# letter_one: The letter in the random word
# storage:  This is where the word/letters will be stored when it is guessed
# guess_attempts: This is where the user is asked to guess a letter
# letter_two: The storage for the random words that is chosen



# 1- Lists that are needed
words = ["Kenya","Germany", "France", "China", "Mexico", "Senegal"]
valid_inputs = list(string.ascii_letters)
print(valid_inputs)
correct_inputs = []
missed = []
storage = []
life_points = 10

# 2- pick a random word from the list
random_words = random.choice(words)

# 3- find the length of the random word
add_length = " "
word_length = len(random_words)
for underscore in range (word_length):
    add_length = add_length + "_"
print(add_length)

# 4- look at the letters in the word
for letter_one in random_words:
    print(letter_one)

# 4- Start the game loop
while True:
    # Ask the user to guess a letter
    guess_attempts = input("Guess a letter:")
    # Stop the loop when done guessing
    if guess_attempts == "done":
        break
    # if the letter is not a valid inputs
    elif guess_attempts not in valid_inputs:
        print("Error, Sorry that's an invalid input!")
    # Otherwise, continue with the game
    else:
        # Check if the letter is in the word
        if guess_attempts in list(random_words):
            # If yes, put it in the correct position
            for w in storage:
                if list(random_words) == guess_attempts:
                    correct_inputs.append(guess_attempts)
            if len(correct_inputs) == len(random_words):
                print("You Win, Great Job you guessed the word!")
                break
        else:
            # If letter not in the word reduce guesses by 1
            life_points -= 1
            # Update the number of guesses
            print(f"guesses left: {life_points}")
            missed.append(words)
            # if all 10 guesses are used up
            if len(missed) == 10:
                print("Game Over")
                break
            # remove the letter from the valid inputs list
            valid_inputs.remove(guess_attempts)
            print("Incorrect, Guess Again!")

