from tkinter import *
import random


# TIC TAC TOE GAME
# Steps:
# Step 1: initialize all the lists as empty
# Step 2: List will be needed with 9 numbers
# - Step 3: Ask the user if they want to play tic-tac-toe
# - If yes continue to the rest of code, if no exit the game
# - Step 4: randomize whoever starts either CPU or user
# - Step 5: pick a letter either x or o
# -There are 9 places, so user and CPU have to choose a space
# - Step 6: prompt where the user wants to place their choice between 1 and 9
# # - Step 7: Check If a spot is free (if not it should have been stored)
# # - Step 8:  Check if there is a winner (function)
#
# spaces = [" "," ", " ", " ", " ", " ", " ", " ", " " ]
# play = input("Would you like to play tic tac toe?")
# random_order= random.choice(player)
# print("This player will start first", random_order)
#  while True:
#     if play == "yes":
#         print("continue")
#     else:
#         break
#
#
'''
def check_empty(spot):
    if game_list[spot] == " ":
       game_list[spot] = "X"
    else:
        print("Sorry,this spot is taken already!")
        continue
'''



game = True
round = False


root = Tk()
# We need 9 squares in a window
root.title("Tic Tac Toe")
root.geometry("300x300")
root['padx'] = 50 # Horizontal padding
root['pady'] = 20 # Vertical padding


# This is for draw
def check_draw():
    if " "  not in game_list:
        return True
    else:
        return False

def check_winner():
 # global game = True
    if game_list[0] == game_list[1] == game_list[2] == "X" or \
        game_list[3] == game_list[4] == game_list[5] == "X" or \
        game_list[6] == game_list[7] == game_list[8] == "X" or \
        game_list[2] == game_list[5] == game_list[7] == "X" or \
        game_list[0] == game_list[4] == game_list[8] == "X" or \
        game_list[0] == game_list[3] == game_list[6] == "X" or \
        game_list[1] == game_list[4] == game_list[7] == "X" or \
        game_list[2] == game_list[5] == game_list[8] == "X":
        print("You Win!")
        return True
 # This is checking not registering
    if game_list[0] == game_list[1] == game_list[2] == "O" or \
        game_list[3] == game_list[4] == game_list[5] == "O" or \
        game_list[6] == game_list[7] == game_list[8] == "O" or \
        game_list[2] == game_list[5] == game_list[7] == "O" or \
        game_list[0] == game_list[4] == game_list[8] == "O" or \
        game_list[0] == game_list[3] == game_list[6] == "O" or \
        game_list[1] == game_list[4] == game_list[7] == "O" or \
        game_list[2] == game_list[5] == game_list[8] == "O":
        print("Computer has Won!")
        return True

    else:
        return False

game_list = [" "," ", " ", " ", " ", " ", " ", " ", " "]
def board():
    # print(game_list[3])
    print(game_list[0],"|",game_list[1],"|",game_list[2])
    print("---+---+---")
    print(game_list[3],"|",game_list[4],"|",game_list[5])
    print("---+---+---")
    print(game_list[6],"|",game_list[7],"|",game_list[8])
    print("           ")
   # print(game_list)

def gui():
    num = 0
    for rowi in range(3):
        for colj in range(3):
            num += 1
            # add a button & size
            button = Button(root, text = num, height = 5, width = 10)
            # grid
            button.grid(row = rowi, column = colj)
            print(f"The value of the column is {colj}")
            print(f"The value of the row is {rowi}")

    root.mainloop()


user_play = input("Would you like to play tic-tac-toe?").lower()
while game:
    if user_play == "yes":
     #  print("continue")
        game = True
    elif user_play == "no":
        break
        #game = False
    else:
        break
       #game = False

     #print(game)
    # print(user_play)

    empty_spot = int(input("Choose a spot between the numbers (1-9):"))

    if game_list[empty_spot-1] == " ":
        game_list[empty_spot-1] = "X"
      # board()
        gui()
    else:
        print("Sorry,this spot is taken already!")
        continue
     # print(game)
    # check_empty(empty_spot)
    winner = check_winner()
     # print(winner)
# if we have winner
    if winner == True:
         game = False
         print("The game has winner")
    else:
        game = True
        # if we have draw
        if check_draw() == True:
            print("There is a draw")
            game = False
        else:
            game = True
            random_number = random.randint(1, 9)
            # print(random_number)
            if game_list[random_number - 1] == " ":
                game_list[random_number - 1] = "O"
                board()
                winner2 = check_winner()
               # print(winner2)
                if  winner2 == True:
                    print("We have a winner")
                    game = False
                else:
                    draw2 = check_draw()
                    if draw2 == True:
                        print("Its a draw")
                        game = False
                    else:
                        game = True
            else:
                print("Sorry computer, spot is taken")
                round = True

                while game_list[random_number - 1] != " " and round == True:
                    random_number = random.randint(1, 9)
                    # print(random_number)
                    if game_list[random_number - 1] == " ":
                        game_list[random_number - 1] = "O"
                        round = False
                        board()
                        # if there is a winner
                        winner3 = check_winner()
                        print(winner3)
                        if winner3 == True:
                            print("We have a winner")
                            game = False
                        else:
                            draw3 = check_draw()
                            if draw3 == True:
                                print("Its a draw")
                                game = False
                            else:
                                game = True
                    else:
                        print("It's not a empty spot Mr Computer")

