import game_functionality
player_wins = 0
player_ties = 0
player_losses = 0
choice = input("would you like to play tic tac toe?\nEnter 1 for yes\nEnter 2 to leave the game\n")
playing = True
while playing:
    if choice == "1":
        game = game_functionality.tic_tac_toe()
        game.play()
        choice = input("Would you like to play again?\nEnter 1 for yes\nEnter 2 to quit\n")
       

    elif choice == "2":
        playing = False

    else:
        choice = input("Please enter a valid choice:\nenter 1 to play again\nenter 2 to leave the game\n")
print("Bye")