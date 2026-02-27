import random

# 1- list with words in variable
words = ["Kenya","Germany", "France", "China", "Mexico", "Senegal"]

# 2- pick a random word from the list
random_words = random.choice(words)
 # print(random_words)

# 3- look at the letters in the word | letter_one is the letter in the random word
for letter_one in random_words:
    print(letter_one)

# 4- Ask the Player to guess a letter
guess_attempts = input("Guess a letter:")

# 5- Compare the players letter to the words letters | letter_two is the storage for the random word chosen
for letter_two in random_words:
    if letter_two == guess_attempts:
        print("right letter!")
    else:
        print("wrong letter!")

# 6- if letter is in word ,print that's right!

# 7- when  its right the letter must hold its place in the word

# 8- else print not right!

# 9- when not right the life counts will have a limit of 10

# 10- when limit exceeded print games over!

