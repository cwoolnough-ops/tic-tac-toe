class tic_tac_toe():
    def __init__(self):
        self.initialize_game()

    def initialize_game(self):
        self.current_board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

        self.current_player = "x"

    #accesses board spaces by indexing and formats them into a game board, prints to console for user to see
    def draw_board(self):
        print("_______________________________\n")
        print('{}|{}|{}'.format(
            self.current_board[0][0], self.current_board[0][1], self.current_board[0][2]))
        print('-+-+-')
        print('{}|{}|{}'.format(
            self.current_board[1][0], self.current_board[1][1], self.current_board[1][2]))
        print('-+-+-')
        print('{}|{}|{}'.format(
            self.current_board[2][0], self.current_board[2][1], self.current_board[2][2]))
        print("_______________________________")

    # checks to see if an ending condition is met
    def is_over(self):
        # horizontal wins
        for i in range(0, 3):
            if (self.current_board[i] == ['x', 'x', 'x']):
                return 'x'
            elif (self.current_board[i] == ['o', 'o', 'o']):
                return 'o'

        # vertical wins
        for i in range(0, 3):
            if self.current_board[0][i] != ' ' and self.current_board[0][i] == self.current_board[1][i] and self.current_board[2][i] == self.current_board[0][i]:
                return self.current_board[0][i]

        # diagonal wins
        if self.current_board[0][0] != ' ' and self.current_board[0][0] == self.current_board[1][1] and self.current_board[1][1] == self.current_board[2][2]:
            return self.current_board[0][0]
        if self.current_board[0][2] != ' ' and self.current_board[0][2] == self.current_board[1][1] and self.current_board[1][1] == self.current_board[2][0]:
            return self.current_board[0][2]

        # is there room?
        for i in range(0, 3):
            for j in range(0, 3):
                if self.current_board[i][j] == ' ':
                    return None

        #if no other returns are met game is a tie
        return " "

    #called on user moves to ensure input is a valid move
    def valid_move(self, x, y):
        if x in ["0", "1", "2"] and y in ["0", "1", "2"] and self.current_board[int(x)][int(y)] == ' ':
            return True
        return False

    #minimax algorithm for the maximizing player works recursively
    def minimax(self):
        
        max = -2 # lower than any possible value returned by the function 
        x_value_1 = None # x coordinate of the move
        y_value_1 = None # y coordinate of the move
        result = self.is_over() # used in the base case below 

        # 3 different base cases, sets the max value to -1 for an x win (oppenent of ai), 1 for ai win, 0 for tie see lower for more return information
        if result == 'x':
            return (-1, 0, 0) 
        if result == 'o':
            return (1, 0, 0)
        if result == ' ':
            return (0, 0, 0)

        # loops through all possible board spaces
        for i in range(0, 3):
            for j in range(0, 3):
                # if the board space is empty make the move in the board space
                if self.current_board[i][j] == ' ':
                    self.current_board[i][j] = 'o'
                    m, i_min, j_min = self.maximin() # m= the value returned from the base case, i_min/j_min are just place holders for the other values returned
                    if m > max: # if the value returned from the base case is greater than our current max update the coordinates of our move 
                        max = m
                        x_value_1 = i
                        y_value_1 = j
                    self.current_board[i][j] = ' ' # used to cleasr the board of the move we made
        return [max, x_value_1, y_value_1] # max is used to retain the value of our move, x_value and Y_value are used to contain the move

    #helper function to minimax algorithm, plays the optimal position for the user to input see minimax for detailed commenting
    def maximin(self):
        min = 2
        x_value_2 = None
        y_value_2 = None
        result = self.is_over()

        if result == 'x':
            return (-1, 0, 0)
        if result == 'y':
            return (1, 0, 0)
        if result == ' ':
            return (0, 0, 0)

        for i in range(0, 3):
            for j in range(0, 3):
                if self.current_board[i][j] == ' ':
                    self.current_board[i][j] = 'x'
                    m, i_max, j_max = self.minimax()
                    if m < min:
                        min = m
                        x_value_2 = i
                        y_value_2 = j
                    self.current_board[i][j] = ' '
        return [min, x_value_2, y_value_2]

    # runs the game
    def play(self):
        while True:
            self.draw_board()

            self.result = self.is_over()

            # prints out the result of the game
            if self.result == " ":
                return print("the game is a tie")
            elif self.result != None:
                return print(self.result + " won the game")

            # checks if its the users turn
            if self.current_player == 'x':
                while True:
                    x = input("input the x coordinate\n")
                    y = input("input the y coordinate\n")
                    if self.valid_move(x, y):
                        self.current_board[int(x)][int(y)] = 'x'
                        self.current_player = 'o'
                        break #ends the turn by making the move and changing what player is up next breaks out of the current loop
                    else:
                        print("please enter valid coordinates")

            # computers move
            else:
                m, x, y = self.minimax() #runs the minimax algorithm
                self.current_board[x][y] = 'o' # makes the move the algorithm choses
                self.current_player = 'x'

