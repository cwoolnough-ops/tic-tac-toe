# string is formatted in a way that the board will keep alignment
player_1 = " x "
player_2 = " o "

# dictionary for storing board values gets updated by moves() and gets shown by game()
board_dict = {"TL": "   ", "TM": "   ", "TR": "   ", "ML": "   ", "MM": "   ", "MR": "   ", "BL": "   ", "BM": "   ", "BL": "   "}
 
# stores number of moves in game, used in end() to end the game if the baoard is full
moves = 0

#put x or o in game board at location user chooses
def move(move, player):
    #holds values of board spaces
    #moves += 1
    board_dict[move] = player

#shows tic tac toe board with values for each space
def show_location_names():
    board = """
     TL | TM | TR 
    ----+----+----
     ML | MM | MR    
    ----+----+----
     BL | BM | BR   """
    print("___________________________")
    print(board)
    print("___________________________")

show_location_names()
print(board_dict)
move("TR", player_1)
print(board_dict)
