import os #clr screen
import random 
import time #sleep
import getpass #hides entered fields


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_valid_gamemode():
    while True:
        try:
            print("〚 Welcome to ROCK, PAPER, SCISSORS 〛")
            gamemode = int(input("〢⟹  Choose a gamemode:\n 1. 🤖 ➠ Play against BOT\n 2. 👤 ➠ Play against PLAYER\n"))
            if gamemode in [1, 2]:
                return gamemode
            else:
                print("❌ ⤿ Invalid input! Please enter 1 or 2.")
                time.sleep(1)
                clear_screen()
        except ValueError:
            print("❌ ⤿ Invalid input! Please enter a valid number (1 or 2).")
            time.sleep(1)
            clear_screen()

def play_bot_game():
    game_list = ['r', 'p', 's']
    player_wins = 0
    bot_wins = 0
    games_played = 0

    while True:
        clear_screen()
        print("🗿 ┋ Rock")
        time.sleep(0.5)
        print("🧻 ┋ Paper")
        time.sleep(0.5)
        print("✂️  ┋ Scissors")
        time.sleep(0.5)
        bot_move = random.choice(game_list)
        player_move = input("Enter your move: (R, P, or S)").lower()
        if player_move not in game_list:
            print("❌ ⤿ Invalid move! Please enter R, P, or S.")
            time.sleep(1)
            continue
        if player_move == bot_move:
            print("🤝 ┋ Tie!")
        elif ((player_move == 'r' and bot_move == 's') or
              (player_move == 'p' and bot_move == 'r') or
              (player_move == 's' and bot_move == 'p')):
            print("🥇 ┋ You win!")
            player_wins += 1
        else:
            print("💔 ┋ You lose!")
            bot_wins += 1
        print(f"The bot's move was {bot_move}!")
        games_played += 1
        print(f"Games played: {games_played}, Your wins: {player_wins}, Bot's wins: {bot_wins}")
        play_again = input("Do you want to play again? (y/n)\n")
        if play_again.lower() != 'y':
            print("Goodbye!")
            break

def play_player_game():
    player1 = input("Enter your name!\n")
    player2 = input(f"Enter Player 2's name: (Player 1's name is {player1})\n")
    print(f"Welcome {player2}")
    time.sleep(1)
    clear_screen()
    game_list = ['r', 'p', 's']
    player1_wins = 0
    player2_wins = 0
    games_played = 0

    while True:
        clear_screen()
        print("🗿 ┋ Rock")
        time.sleep(0.5)
        print("🧻 ┋ Paper")
        time.sleep(0.5)
        print("✂️  ┋ Scissors")
        time.sleep(0.5)
        # Use getpass for player moves to hide input
        player1_move = getpass.getpass(f"Enter your move {player1}: (R, P, or S)[Input is hidden!]").lower()
        player2_move = getpass.getpass(f"Enter your move {player2}: (R, P, or S)[Input is hidden!]").lower()
        if player1_move not in game_list or player2_move not in game_list:
            print("❌ ⤿ Invalid move! Please enter R, P, or S.")
            time.sleep(1)
            continue
        if player1_move == player2_move:
            print("🤝 ┋ Tie!")
        elif ((player1_move == 'r' and player2_move == 's') or
              (player1_move == 'p' and player2_move == 'r') or
              (player1_move == 's' and player2_move == 'p')):
            print(f"🥇 ┋ {player1} wins!")
            player1_wins += 1
        else:
            print(f"🥇 ┋ {player2} wins!")
            player2_wins += 1
        games_played += 1
        print(f"{player1} went {player1_move} and {player2} went {player2_move}! ")
        print(f"--¦ Games played: {games_played}, {player1}'s wins: {player1_wins}, {player2}'s wins: {player2_wins}")
        play_again = input("Do you want to play again? (y/n)")
        if play_again.lower() != 'y':
            print("Goodbye!")
            break

def main():
    clear_screen()
    selected_mode = get_valid_gamemode()
    print(f"You selected gamemode {selected_mode}")
    time.sleep(1)
    if selected_mode == 1:
        play_bot_game()
    else:
        play_player_game()

if __name__ == "__main__":
    main()
