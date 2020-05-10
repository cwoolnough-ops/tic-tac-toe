#this file is used as a main menu to the game 
import game_functionality
choice = input("Welcome to tic tac toe tournament!\nEnter 1 to start a tournament\nEnter 2 to leave the game\n")

#used to keep asking the player if he wants to start a new tournament
playing = True

while playing:
    #initializes game 
    if choice == "1":
        game = game_functionality.tic_tac_toe()
        game.play()

        #if a tournament is exited asks if you would like to start a new tournament
        choice = input("Would you like to start a new tournament?\nEnter 1 for yes\nEnter 2 to quit\n")
        
    #stops the game
    elif choice == "2":
        playing = False

    #ensure correct input
    else:
        choice = input("Please enter a valid choice:\nenter 1 to start a tournament\nenter 2 to leave the game\n")
# goodbye message if game is stopped
print("Bye, thanks for playing.")
