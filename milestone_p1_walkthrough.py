import random
# MILESTONE PROJECT 1 (PRACTICE ROUND)
# Create a TIC TAC TOE game

### Displaying the TIC TAC TOE BOARD
# STEP 1:  Write a function that can print out a board. Set up your board as a list, where each index 1-9
# corresponds with a number on a number pad, so you get a 3 by 3 board representation.
def display_board(board):   # Here we define the function as display_board where the parameter is the board
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('------------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('------------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
#Test STEP 1 -- run your function on a test version of the board list, and make adjustments as necessary
test_board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
display_board(test_board)

### Player's input for the TIC TAC TOE BOARD GAME
# Step 2: Write a function that can take in a player input and assign their marker as 'X' or 'O'.
# Think about using while loops to continually ask until you get a correct answer.
def player_input():
    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input("Player 1: Do you want X or O:  ").upper()

    # Returns a Tuple assignment
    if marker == 'X':
        return ('X', 'O')
    else:
        return('O', 'X')

player_input()

### Assigning a Marker to the board
# Step 3: Write a function that takes in the board list object, a marker ('X' or 'O'),
# and a desired position (number 1-9) and assigns it to the board.
def place_marker(board, marker, position):
    board[position] = marker

# TEST Step 3: run the place marker function using test parameters and display the modified board
place_marker(test_board, '$', 8)
display_board(test_board)

# Step 4: Write a function that takes in a board and checks to see if someone has won.
def win_check(board, mark):
    # WIN TIC TAC TOE???

    # ALL ROWS, and check to see if they all share the same marker?

    # ALL COLUMNS , check to see if marker matches
    # 2 diagonals, check to see match

    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the left side
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

# Test Step 4: run the win_check function against our test_board - it should return True
print(win_check(test_board, 'X'))

### PLAYER 1 or PLAYER 2: WHO WILL GO FIRST
# Step 5: Write a function that uses the random module to randomly decide which player goes first.
def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

# Step 6: Write a function that returns a boolean indicating whether a space on the board is freely available.
def space_check(board, position):

    return board[position] == ' '

# Step 7: Write a function that checks if the board is full and returns a boolean value. True if full, False otherwise.
def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True

# Step 8: Write a function that asks for a player's next position (as a number 1-9) and
# then uses the function from step 6 to check if it's a free position. If it is, then return the position for later use.
def player_choice(board):
    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position (1-9):  '))

    return position

# Step 9: Write a function that asks the player if they want to play again and returns a boolean True if they do want to play again.
def replay():

    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

# WHILE LOOP TO KEEP RUNNING THE GAME

# Final Part: Use While loops and the functions you've made to run the game!
print('Welcome to Tic Tac Toe!')

while True:
    # PLAY THE GAME

    ## SET EVERYTHING UP (BOARD, WHOS FIRST, CHOOSE MARKERS X, O )
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first!')

    ## GAME PLAY
    play_the_game = input(("You ready to play??? Yes or No: "))
    if play_the_game.lower()[0] == 'y':
        game_start = True
    else:
        game_start = False

    ### PLAYER ONE TURN

    while game_start:
        if turn == 'Player 1':

            # Show the Board
            display_board(theBoard)
            # Choose a position
            position = player_choice(theBoard)
            # Place the marker on the position
            place_marker(theBoard, player1_marker, position)

            # Check if they won
            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations!! You have won the game!!! You win a $50 giftcard to Hollister!!')
                game_start = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print("It's a Draw!!!")
                    break
                else:
                    turn = 'Player 2'   # No tie and no winner? Then next player's turn
        else:
            ### PLAYER TWO TURN

            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!!! You win a $50 giftcard to Hollister!!')
                game_start = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print("It's a Draw!!!")
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break
    # BREAK OUT OF THE WHILE LOOP ON replay()