import random
while True:
    # ask player would they like to play game
    game = input(f"Would you like to play rock, paper, scissors?").lower()
    if game == "no":
        break
    else:
        # ask player what do they want to be
        player_choice = input("What object do you want to be? rock = 0, paper = 1, scissors = 2: ")
        print("Player Choice:",player_choice)
        # cpu picks randomly its choice
        cpu_choice = [0,1,2]
        random_cpu = random.choice(cpu_choice)
        print("Computer Choice:",random_cpu)
# compare the player and computer
        # If player and CPU have the same number
        if player_choice == cpu_choice:
            print("Its a draw!")
        # If CPU has chooses 0 and player chooses 1
        elif cpu_choice == 0 and player_choice == 1:
            print("Player Wins!")

# if CPU chooses 0 and player chooses 2
# if CPU chooses 0 and player chooses 3

# if CPU chooses 1 and player chooses 2
# if CPU chooses 1 and player chooses 3

# if CPU has chooses 2 and player chooses 1
# if CPU chooses 2 and player chooses 3

# if CPU has chooses 3 and player chooses 1
# if CPU chooses 3 and player chooses 2



