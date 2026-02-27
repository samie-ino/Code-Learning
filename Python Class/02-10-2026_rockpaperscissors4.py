import random
while True:
    # ask player would they like to play game
    game = input(f"Would you like to play rock, paper, scissors?").lower()
    if game == "no":
        break
    else:
        # ask player what do they want to be
        player_choice = int(input("What object do you want to be? rock = 0, paper = 1, scissors = 2: "))
        print("Player Choice:",player_choice)
        # cpu picks randomly its choice
        cpu_choice = [0,1,2]
        random_cpu = random.choice(cpu_choice)
        print("Computer Choice:",random_cpu)
    # compare the player and computer
        numbers = [0,1,2]
        if player_choice not in numbers:
            print("Error invalid input!")
        # If player and CPU have the same number
        elif random_cpu == player_choice:
            print("Its a draw!")
    # If CPU has chooses 0 and player chooses 1
        elif random_cpu == 0 and player_choice == 1:
            print("Player Wins!")
        # if CPU chooses 0 and player chooses 2
        elif random_cpu == 0 and player_choice == 2:
            print("CPU Wins!")
        # if CPU chooses 1 and player chooses 0
        elif random_cpu == 1 and player_choice == 0:
            print("CPU Wins!")
        # if CPU has chooses 1 and player chooses 2
        elif random_cpu == 1 and player_choice == 2:
            print("Player Wins!")
        # if CPU chooses 2 and player chooses 0
        elif random_cpu == 2 and player_choice == 0:
            print("Player Wins!")
        # if CPU has chooses 2 and player chooses 1
        elif random_cpu == 2 and player_choice == 1:
            print("CPU Wins!")


