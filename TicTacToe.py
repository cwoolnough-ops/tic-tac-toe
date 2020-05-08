import game_functions
def game():
    print("Lets play tic tac toe")
    #assigns player names
    game_functions.player_1[1] = input("\nwrite the name of player 1 \n")
    game_functions.player_2[1] = input("\nwrite the name of player 2 \n")
    # introduces the players and tells game rules
    print("\n"+ game_functions.player_1[1] + " goes first as" + game_functions.player_1[0] + "and is playing against " + game_functions.player_2[1] + " as o")
    print("\nIn tic tac toe players take turns marking a spot on the board \n\nTo win the game a player must get a line either horizontally, diagonally or vertically \n\nHere is the board:")
    game_functions.show_location_names()
    print("the numbers reffer to the key you must enter to mark that space on the board")
    # unused variable, used as a gate to start the game
    start = input("press any key to start the game! \n")
    # continualy asks for player moves untill an ending condiition is met ie: is_game_over
    last_move = game_functions.player_2
    filled_spots = []
    valid_choices = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    while game_functions.is_game_over(game_functions.board_dict) == 0:
        if last_move == game_functions.player_2:
            current_player = game_functions.player_1
        else:
            current_player = game_functions.player_2
        last_move = current_player
        game_functions.show_location_names()
        game_functions.current_board()
        choice = input(current_player[1] + "(" + current_player[0] + ") it is your turn where would you like to play? \npress the number where you want to play then the \"enter\" key \n")
        while choice in filled_spots or choice not in valid_choices:
            if choice in filled_spots:
                choice = input("that space is filled please try again\n")
            elif choice not in valid_choices:
                choice = input("please chose a valid space\n")
        game_functions.move(choice, current_player)
        # last_move = current_player
        filled_spots += choice
    if game_functions.is_game_over(game_functions.board_dict) == 1:
        print("\n" + last_move[1] + " Wins!")
    else:
        print("\nThe game ends with a tie")
game()
