import game_functionality
choice = input("Welcome to tic tac toe tournament!\nEnter 1 to start\nEnter 2 to leave the game\n")
playing = True
while playing:
    if choice == "1":
        game = game_functionality.tic_tac_toe()
        game.play()
        choice = input("Would you like to start a new tournament?\nEnter 1 for yes\nEnter 2 to quit\n")
        

    elif choice == "2":
        playing = False

    else:
        choice = input("Please enter a valid choice:\nenter 1 to play again\nenter 2 to leave the game\n")
print("Bye")
