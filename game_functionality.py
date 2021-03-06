
class tic_tac_toe():
    def __init__(self):
        self.initialize_game()

    def initialize_game(self):
        self.current_board = [['   ', '   ', '   '], ['   ', '   ', '   '], ['   ', '   ', '   ']]

        self.current_player = " x "
        self.x_wins = 0
        self.ties = 0
        self.o_wins = 0

    #accesses board spaces by indexing and formats them into a game board, prints to console for user to see
    def draw_board(self):
        print("_______________________________\n")
        print('x > 0   1   2\n')
        # print('______________') 
        print('0  {}|{}|{}'.format(
            self.current_board[0][0], self.current_board[0][1], self.current_board[0][2]))
        print('   ---+---+---')
        print('1  {}|{}|{}'.format(
            self.current_board[1][0], self.current_board[1][1], self.current_board[1][2]))
        print('   ---+---+---')
        print('2  {}|{}|{}'.format(
            self.current_board[2][0], self.current_board[2][1], self.current_board[2][2]))
        print("^")
        print("y")
        print("_______________________________")

    # checks to see if an ending condition is met
    def is_over(self):
        # horizontal wins
        for i in range(0, 3):
            if (self.current_board[i] == [' x ', ' x ', ' x ']):
                return ' x '

            elif (self.current_board[i] == [' o ', ' o ', ' o ']):
                return ' o '

        # vertical wins
        for i in range(0, 3):
            if self.current_board[0][i] != '   ' and self.current_board[0][i] == self.current_board[1][i] and self.current_board[2][i] == self.current_board[0][i]:
                return self.current_board[0][i]

        # diagonal wins
        if self.current_board[0][0] != '   ' and self.current_board[0][0] == self.current_board[1][1] and self.current_board[1][1] == self.current_board[2][2]:
            return self.current_board[0][0]
        if self.current_board[0][2] != '   ' and self.current_board[0][2] == self.current_board[1][1] and self.current_board[1][1] == self.current_board[2][0]:
            return self.current_board[0][2]

        # is there room?
        for i in range(0, 3):
            for j in range(0, 3):
                if self.current_board[i][j] == '   ':
                    return None

        #if no other returns are met game is a tie
        return "   "

    #called on user moves to ensure input is a valid move
    def valid_move(self, x, y):
        if x in ["0", "1", "2"] and y in ["0", "1", "2"] and self.current_board[int(x)][int(y)] == '   ':
            return True
        return False

    #minimax algorithm for the maximizing player works recursively
    def minimax(self):
        
        max = -2 # lower than any possible value returned by the function 
        x_value_1 = None # x coordinate of the move
        y_value_1 = None # y coordinate of the move
        result = self.is_over() # used in the base case below 

        # 3 different base cases, sets the max value to -1 for an x win (oppenent of ai), 1 for ai win, 0 for tie see lower for more return information
        if result == ' x ':
            return (-1, 0, 0) 
        if result == ' o ':
            return (1, 0, 0)
        if result == '   ':
            return (0, 0, 0)

        # loops through all possible board spaces
        for i in range(0, 3):
            for j in range(0, 3):
                # if the board space is empty make the move in the board space
                if self.current_board[i][j] == '   ':
                    self.current_board[i][j] = ' o '
                    m, i_min, j_min = self.maximin() # m= the value returned from the base case, i_min/j_min are just place holders for the other values returned
                    if m > max: # if the value returned from the base case is greater than our current max update the coordinates of our move 
                        max = m
                        x_value_1 = i
                        y_value_1 = j
                    self.current_board[i][j] = '   ' # used to cleasr the board of the move we made
        return [max, x_value_1, y_value_1] # max is used to retain the value of our move, x_value and Y_value are used to contain the move

    #helper function to minimax algorithm, plays the optimal position for the user to input see minimax for detailed commenting
    def maximin(self):
        min = 2
        x_value_2 = None
        y_value_2 = None
        result = self.is_over()

        if result == ' x ':
            return (-1, 0, 0)
        if result == ' y ':
            return (1, 0, 0)
        if result == '   ':
            return (0, 0, 0)

        for i in range(0, 3):
            for j in range(0, 3):
                if self.current_board[i][j] == '   ':
                    self.current_board[i][j] = ' x '
                    m, i_max, j_max = self.minimax()
                    if m < min:
                        min = m
                        x_value_2 = i
                        y_value_2 = j
                    self.current_board[i][j] = '   '
        return [min, x_value_2, y_value_2]

    #prints out the winning board with the winning line capitilized
    def highlight_winner(self):
        #horizontal wins
        for i in range(0, 3):
            if (self.current_board[i] == [' x ', ' x ', ' x ']):
                self.current_board[i] = [' X ', ' X ', ' X ']
                self.draw_board()
                return

            elif (self.current_board[i] == [' o ', ' o ', ' o ']):
                self.current_board[i] = [' O ', ' O ', ' O ']
                self.draw_board()
                return

        # vertical wins
        for i in range(0, 3):
            if self.current_board[0][i] != '   ' and self.current_board[0][i] == self.current_board[1][i] and self.current_board[2][i] == self.current_board[0][i]:
                new_vert = self.current_board[0][i].upper()
                self.current_board[0][i] = new_vert 
                self.current_board[1][i] = new_vert 
                self.current_board[2][i] = new_vert
                self.draw_board()
                return

        # diagonal wins
        if self.current_board[0][0] != '   ' and self.current_board[0][0] == self.current_board[1][1] and self.current_board[1][1] == self.current_board[2][2]:
            new_diag_1 = self.current_board[0][0].upper()
            self.current_board[0][0] = new_diag_1
            self.current_board[1][1] = new_diag_1
            self.current_board[2][2] = new_diag_1
            self.draw_board()
            return
        if self.current_board[0][2] != '   ' and self.current_board[0][2] == self.current_board[1][1] and self.current_board[1][1] == self.current_board[2][0]:
            new_diag_2 = self.current_board[0][2].upper()
            self.current_board[0][2] = new_diag_2
            self.current_board[1][1] = new_diag_2
            self.current_board[2][0] = new_diag_2
            self.draw_board()
            return

    # runs the game
    def play(self):
        # asks if player wants to play a friend or the computer
        self.two_player = input("\nWould you like to play against a friend or the computer?\nenter f for friend\nenter c for computer\n")
        self.valid_options = ["c", "f"]
        #ensures correct input
        while self.two_player not in self.valid_options:
            self.two_player = input("please enter a valid choice\nenter f to play a friend\nenter c to play the computer\n")

        # game only ends if return statements are met in line 224/229 or playgame() is called in line 216
        while True:
            self.result = self.is_over()
            
            # if the game is still running print the game board
            if self.result == None:
                self.draw_board()

            #from here untill line "229" are conditions to run if the game is finished
            elif self.result != None:
                #for a tie game
                if self.result == "   ":
                    self.ties += 1
                    self.draw_board()
                    print("The game is a tie")

                # for an O win
                elif self.result == " o ":
                    self.o_wins += 1
                    self.highlight_winner()
                    print("O wins the game\n")
                    print("The winning line is capitalized\n")
                
                #for an X win
                else:
                    self.x_wins += 1
                    self.highlight_winner()
                    print("X wins the game\n")
                    print("The winning line is capitalized\n")

                #asks if the user wants to continue playing
                play_again = input("Would you like to continue the tournament?\nEnter 1 for yes\nenter 2 for no\n")

                #ensures user enters correct input
                while play_again not in ["1", "2"]:
                    play_again = input("Please enter a valid choice\nEnter 1 for to continue the tournament\nenter 2 to stop the tournament\n")
                
                # if the user wants to play again show the tournament score and start a new game
                if play_again == "1":
                    self.clear_board()
                    
                    #shows the current tournament score
                    print("\nThe Tournament score is:\nX wins: {}   O wins: {}   ties: {}\n".format(str(self.x_wins), str(self.o_wins), str(self.ties)))
                    
                    #starts a new game
                    self.play()

                #shows final tournament score and exits to main menu
                elif play_again == "2":
                    
                    #final score
                    print("\nThe final tournament score is:\nX wins: {}   O wins: {}   ties: {}\n".format(str(self.x_wins), str(self.o_wins), str(self.ties)))
                    
                    return
                
                #second return statement here to fix bug where if game starts as a 2 player game then user chooses
                #to face the computer it will not fully exit the game unless user choses to end the game twice
                # this return is avoided if the user choses to play again by the self.play() call
                return

            # two player game
            if self.two_player == "f":
                #ensure game is not over
                while self.is_over() == None:
                    #tells what players turn it is
                    print("{} its your turn".format(self.current_player[1]))

                    # gets the users move
                    x = input("input the x coordinate\n")
                    y = input("input the y coordinate\n")
                    
                    # checks for valid moves, makes the move if valid
                    if self.valid_move(x, y):
                        self.current_board[int(x)][int(y)] = self.current_player

                        #after move is made change whos turn it is
                        if self.current_player == ' o ':
                            self.current_player = ' x '
                        else:
                            self.current_player = ' o '
                        self.draw_board()
                    else:
                        print("please enter valid coordinates")
                
            # checks if its the users turn in an ai game most of the functionality is described in 2 player game
            if self.current_player == ' x ' and self.two_player == "c" and self.is_over() == None:
                while True:
                    print("x its your turn")
                    x = input("input the x coordinate\n")
                    y = input("input the y coordinate\n")
                    if self.valid_move(x, y):
                        self.current_board[int(x)][int(y)] = ' x '
                        self.current_player = ' o '
                        break #ends the turn by making the move and changing what player is up next breaks out of the current loop
                    else:
                        print("please enter valid coordinates")
            
            # computers move 
            if self.current_player == ' o ' and self.two_player == 'c' and self.is_over() == None:
                m, x, y = self.minimax() #runs the minimax algorithm
                self.current_board[x][y] = ' o ' # makes the move the algorithm choses
                self.current_player = ' x '
    
    #clears the board
    def clear_board(self):
        for i in range(3):
            for j in range(3):
                self.current_board[i][j] = '   '
                self.current_player = ' x '
