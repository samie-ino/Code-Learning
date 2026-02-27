import random
from typing import Any

# 1- list with words in variable
words = ["Kenya","Germany", "France", "China", "Mexico", "Senegal"]

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
#storage = " "
while True:
    #found_letters = []
    storage = " "
    print("storage --", storage)
    print(found_letters)
    guess_attempts = input("Guess a letter:")
    for letter_two in random_words:
        if letter_two == guess_attempts:
            storage += letter_two
            found_letters.append(letter_two)
           # print("letter found", storage)
        elif guess_attempts in found_letters:
            storage += guess_attempts
            # print("letter already found", storage)
        else:
            storage += "_"
            # print("letter not found", storage)

    print("storage at the end of the loop", storage)

# 5-create an empty list here and then link it to the storage
    #attach = []
    #attach = storage





# 6- life counts will have a limit of 10| limit exceeded print games over!
    limit = 0
    if limit >= 10:
        print("Sorry game over you lose!")
    else:
        print("Keep trying dont give up!")
