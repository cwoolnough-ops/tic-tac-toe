# string is formatted in a way that the board will keep alignment
player_1 = [" x ", None]
player_2 = [" o ", None]

# dictionary for storing board values, gets updated by moves() and gets shown by game()
board_dict = {"1": "   ", "2": "   ", "3": "   ", "4": "   ", "5": "   ", "6": "   ", "7": "   ", "8": "   ", "9": "   "}
 
# stores number of moves in game, used in is_game_over() to end the game if the board is full
moves = 0

#put x or o in game board at the location user chooses
def move(move, player):
    #holds values of board spaces
    global moves
    moves += 1
    board_dict[move] = player[0]

#shows tic tac toe board with values for each space
def show_location_names():
    board =  """
     1 | 2 | 3 
    ---+---+---
     4 | 5 | 6    
    ---+---+---
     7 | 8 | 9  """
    print("___________________________")
    print(board)
    # print("")
    print("___________________________")
#prints the current state of the game board
def current_board():
    print("current board:\n")
    print("    " + board_dict["1"] + "|" + board_dict["2"] + "|" + board_dict["3"])
    print("    " + "---+---+---")
    print("    " + board_dict["4"] + "|" + board_dict["5"] + "|" + board_dict["6"])
    print("    " + "---+---+---")
    print("    " + board_dict["7"] + "|" + board_dict["8"] + "|" + board_dict["9"])
    print("___________________________")
# tests if any of the ending conditions for tic tac toe are met
def is_game_over(board_dict):
    #values in each line are put into a set, if all values in a line are " x " the set length will be 1, representing a winning line
    horizontal_1 = {board_dict["1"], board_dict["2"], board_dict["3"]}
    horizontal_2 = {board_dict["4"], board_dict["5"], board_dict["6"]}
    horizontal_3 = {board_dict["7"], board_dict["8"], board_dict["9"]}
    
    vertical_1 = {board_dict["1"], board_dict["4"], board_dict["7"]}
    vertical_2 = {board_dict["2"], board_dict["5"], board_dict["8"]}
    vertical_3 = {board_dict["3"], board_dict["6"], board_dict["9"]}
    
    diagonal_1 = {board_dict["1"], board_dict["5"], board_dict["9"]}
    diagonal_2 = {board_dict["3"], board_dict["5"], board_dict["7"]}
    # loop through all lines checking if a line is winning
    for line in [diagonal_1, diagonal_2, horizontal_1, horizontal_2, horizontal_3, vertical_1, vertical_2, vertical_3]:
        if len(line) == 1 and "   " not in line: # ("   " not in line) removes the possibility of an empty line being a win
            return 1
    if moves == 9: #if the win condition is not met and 9 moves are made(filled board), the game is a tie 
        return 2
    return 0 # value of 1 or 0 is used in game function to determine wether to keep asking for input