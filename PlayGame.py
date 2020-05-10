import game_functionality

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
        choice = input("Please enter a valid choice:\n1 to play against a friend\n2 to play against the computer\n3 to leave the game\n")
print("Bye")