import random

# Play one round, return 1=player win, -1=cpu win, 0=tie
def play_round():
    choices = {0: "rock", 1: "paper", 2: "scissors"}

    # Get player choice
    player_choice = int(input("Choose: rock=0, paper=1, scissors=2: "))

    # Validate input
    if player_choice not in [0, 1, 2]:
        print("Invalid! Use 0, 1, or 2.")
        return 0

    # CPU random choice
    cpu_choice = random.choice([0, 1, 2])
    print(f"Player: {choices[player_choice]} | CPU: {choices[cpu_choice]}")

    # Check tie
    if player_choice == cpu_choice:
        print("Tie!")
        return 0

    # Win if (player - cpu) % 3 == 1 (paper>rock, scissors>paper, rock>scissors)
    if (player_choice - cpu_choice) % 3 == 1:
        print("Player wins!")
        return 1
    else:
        print("CPU wins!")
        return -1


# Single round game
def reg_game():
    print("You are playing the regular mode!")
    play_round()


# First to 3 wins (best of 3)
def best_of_three():
    print("You are playing the best out of three mode!")
    player_score, cpu_score = 0, 0

    while player_score < 3 and cpu_score < 3:
        result = play_round()
        if result == 1:
            player_score += 1
        elif result == -1:
            cpu_score += 1
        print(f"Score: Player {player_score} - CPU {cpu_score}\n")

    # Declare final winner
    winner = "You" if player_score == 3 else "CPU"
    print(f"{winner} wins the match!")


# Main menu - choose regular OR best of 3
def main():
    # First question: Do you want to play? (plain print, no f-string)
    reg_choice = input("Would you like to play rock, paper, scissors? ").lower()
    if reg_choice != "yes":
        print("Thanks for playing!")
        return

    # Second question: Regular OR best of 3? (plain print, no f-string)
    three_choice = input("Do you want to play best out of 3? ").lower()
    if three_choice == "yes":
        best_of_three()
    else:
        reg_game()


if __name__ == "__main__":
    main()
