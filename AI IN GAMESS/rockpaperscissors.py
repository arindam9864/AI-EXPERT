import random
from colorama import Fore, init

init(autoreset=True)

choices = ["rock", "paper", "scissors"]

def get_ai_move(player_history):
    if len(player_history) < 2:
        return random.choice(choices)
    last_move = player_history[-1]
    if last_move == "rock":
        return "paper"
    elif last_move == "paper":
        return "scissors"
    else:
        return "rock"

def get_result(player, ai):
    if player == ai:
        return "tie"
    elif (player == "rock" and ai == "scissors") or \
         (player == "paper" and ai == "rock") or \
         (player == "scissors" and ai == "paper"):
        return "win"
    else:
        return "lose"

def play():
    player_history = []
    score_player = 0
    score_ai = 0

    print(Fore.CYAN + "Welcome to Rock Paper Scissors AI Game")

    while True:
        player = input(Fore.YELLOW + "Enter rock, paper, or scissors (or exit): ").lower().strip()

        if player == "exit":
            print(Fore.CYAN + "Final Score -> You:", score_player, "AI:", score_ai)
            break

        if player not in choices:
            print(Fore.RED + "Invalid choice")
            continue

        ai = get_ai_move(player_history)
        player_history.append(player)

        print(Fore.GREEN + f"AI chose: {ai}")

        result = get_result(player, ai)

        if result == "win":
            print(Fore.GREEN + "You win!")
            score_player += 1
        elif result == "lose":
            print(Fore.RED + "AI wins!")
            score_ai += 1
        else:
            print(Fore.BLUE + "It's a tie!")

        print(Fore.CYAN + f"Score -> You: {score_player} | AI: {score_ai}\n")

if __name__ == "__main__":
    play()
