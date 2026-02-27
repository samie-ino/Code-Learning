import random
import string
from hangdude import Tom
from typing import Any
# 1- list with words in variable
words = ["Kenya","Germany", "France", "China", "Mexico", "Senegal"]
valid_inputs = list(string.ascii_letters)
# 2- pick a random word from the list
# Note: You need to know the length of the word
random_words = random.choice(words)
# print(random_words)
add_length = " "

word_length = len(random_words)
for underscore in range (word_length):
    add_length = add_length + "_"
print(add_length)

# 3- look at the letters in the word | letter_one is the letter in the random word
for letter_one in random_words:
    print(letter_one)


# 4- Compare the players letter to the words letters | letter_two is the storage for the random word chosen
# Note:  when its right the letter must hold its place in the word
found_letters = []
life_points = 9

while True:
    storage = " "
    # print("storage --", storage)
    print(found_letters)
# Ask the user to guess a letter
    guess_attempts = input("Guess a letter:")
    for letter_two in random_words:
# Check to see if the guess attempt is in the word
# Note: Lines 36-38  covers if the letter is guessed then added

        if letter_two == guess_attempts:
            storage += letter_two
            found_letters.append(letter_two)


        #elif guess_attempts in found_letters:
            #storage += guess_attempts
        elif letter_two in found_letters:
            storage += letter_two
            # print("letter already found", storage)

        else:
            storage += "_"
# This is if the guess is not in the word
    if guess_attempts not in storage:
            if guess_attempts not in valid_inputs:
                print("Error, This is not a letter!")
            else:
                life_points = life_points - 1  #life_points -= 1
                print(f"Remaining Lives:{life_points}")
                print(Tom[life_points])
                if life_points == 0:
                    print("Game Over!")
                    break
# This is if You filled all the blanks
    if "_" not in storage:
        print("Great Job, You guessed the word!")
        break

            # print("letter not found", storage)
    print(f"value of storage is{storage}")
