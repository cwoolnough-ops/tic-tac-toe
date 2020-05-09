import AiPlayer
import TicTacToe
print("Would you like to play against the computer or a friend?")

choice = input("Enter 1 for friend\nEnter 2 for computer\nEnter 3 to leave the game\n")
playing = True
while playing:
    if choice == "1":
        TicTacToe.two_player_game()
        input("Would you like to play again?\nEnter 1 for yes\nEnter 2 for no\n")
        playing = False

    elif choice == "2":
        game = AiPlayer.tic_tac_toe()
        game.play()
        input("Would you like to play again?\nEnter 1 for yes\nEnter 2 for no\n")
        playing = False

    elif choice == "3":
        playing = False

    else:
        choice = input("Please enter a valid choice:\n1 to play against a friend\n2 to play against the computer\n3 to leave the game\n")
print("Bye")