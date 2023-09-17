import random

def userchoice():
    while True:
        playerchoice = input("What's your Choice?: rock, paper, or scissors: ").lower()
        if playerchoice in ["rock", "paper", "scissors"]:
            return playerchoice
        else:
            print("You chose Invalid option. Please choose between rock, paper, or scissors.")

def cpuchoice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def get_winner(playerchoice, desktop_choice):
    if playerchoice == desktop_choice:
        return "It's a tie!"
    elif (playerchoice == "rock" and desktop_choice == "scissors") or \
         (playerchoice == "scissors" and desktop_choice == "paper") or \
         (playerchoice == "paper" and desktop_choice == "rock"):
        return "You win!!!"
    else:
        return "Computer wins!!!"

def play_game():
    player_score = 0
    cpu_score = 0
    rounds = 0

    while True:
        playerchoice = userchoice()
        desktop_choice = cpuchoice()

        print(f"You chose: {playerchoice}")
        print(f"Computer chose: {desktop_choice}")

        result = get_winner(playerchoice, desktop_choice)
        print(result)

        if "You win" in result:
            player_score += 1
        elif "Computer wins" in result:
            cpu_score += 1
        rounds += 1
        print(f"Score - YOU: {player_score}, COMPUTER: {cpu_score}")
        play_again = input("Wanna play again? (yes/no): ").lower()
        if play_again != "yes":
            print(f"You have played {rounds} rounds. Final score is - YOU: {player_score}, COMPUTER: {cpu_score}")
            break

if __name__ == "__main__":
    print("--------------------ROCK-PAPER-SCISSORS--------------------")
    print("Made By:- Rajib Bishal")
    print("-----------------------------------------------------------")
    play_game()
