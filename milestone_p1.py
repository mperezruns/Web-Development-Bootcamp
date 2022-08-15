import random
### Milestone Project -- TIc Tac Toe Game

# Piece 1 -- Board Display
# Step 1: Write a function that can print out a board. Set up your board as a list, where each index 1-9 corresponds
# with a number on a number pad, so you get a 3 by 3 board representation.

def display_board(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print(' ----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print(' ----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

test_board = ['#', 'X', 'O','X', 'O', 'X', 'O', 'X', 'O', 'X']
display_board(test_board)

# Piece 2 -- Player's input
# Step 2: Write a function that can take in a player input and assign their marker as 'X' or 'O'.
# Think about using while loops to continually ask until you get a correct answer.
def player_input():
    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input("Player 1: Do you want to be X or O:  ").upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

player_input()

# Piece 3 -- Place Marker for 'X' and 'O'
# Step 3: Write a function that takes in the board list object, a marker ('X' or 'O'), and a desired position
# (number 1-9) and assigns it to the board.
def place_maker(board, marker, position):
    board[position] = marker

# Test Step 3: Run the place marker function using test parameters and display the modified board.
place_maker(test_board, '$', 8)
display_board(test_board)

# Piece 4 -- Who is the Winner?
# Step 4: Write a function that takes in a board and a mark (X or O) and then checks to see if that mark has won.

def win_check(board, mark):

    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or
    (board[1] == mark and board[2] == mark and board[3] == mark) or
    (board[7] == mark and board[4] == mark and board[1] == mark) or
    (board[8] == mark and board[5] == mark and board[2] == mark) or
    (board[9] == mark and board[6] == mark and board[3] == mark) or
    (board[7] == mark and board[5] == mark and board[3] == mark) or
    (board[9] == mark and board[5] == mark and board[1] == mark))

print(win_check(test_board, 'X'))

# Piece 5 -- Who goes first???
# Step 5: Write a function that uses the random module to randomly decide which player goes first. You may want to lookup
# random.randint() Return a string of which player went first
def who_goes_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

# Piece 6 -- Space Check
# Step 6: Write a function that returns a boolean indicating whether a space on the board is freely available.
def space_check(board, position):

    return board[position] == ' '

# Piece 7 -- Full Board Check
# HINT -- FOR LOOP
# Step 7: Write a function that checks if the board is full and returns a boolean value. True if full, False otherwise.
def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True

# Piece 8 -- Player selects a position
# Step 8: Write a function that asks for a player's next position (as a number 1-9) and then uses the function from step 6 to check if it's a free position.
# If it is, then return the position for a later use\.
def player_choice(board):
    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your position (1-9): '))

    return position

# Piece 9 -- Reset
# Step 9: Write a function that asks the player if they want to play again and returns a boolean True if they do want to play again.
def replay():

    return input("Do you want to play again?? Enter Yes or No: ").lower().startswith('y')

# Piece 10 -- Combining my functions into a running tic tac toe game!!!!
# Final Part: Use while loops and the functions you've made to run the game!
print('Welcome to Tic Tac Toe!!!')

while True:
    # Set the game up here
    # Here we reset the board for the players
    xoBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = who_goes_first()
    print(turn + ' will go first!!!!')


    play_the_game = input(("Are you ready to Play??? Yes or No: "))
    if play_the_game.lower()[0] == 'y':
        game_begins = True
    else:
        game_begins = False

    # Player 1's Turn
    while game_begins:
        if turn == 'Player 1':


            display_board(xoBoard)
            position = player_choice(xoBoard)
            place_maker(xoBoard, player1_marker, position)

            # If player 1 wins the game
            if win_check(xoBoard, player1_marker):
                display_board(xoBoard)
                print('Congratulations!!!! You have won the game!!! You win a $25 gift card to Starbucks!!!')
                game_begins = False
            else:
                if full_board_check(xoBoard):
                    display_board(xoBoard)
                    print("It's a Draw!!!")
                    break
                else:
                    turn = 'Player 2'
        else:
            # Player Two's turn
            display_board(xoBoard)
            position = player_choice(xoBoard)
            place_maker(xoBoard, player2_marker, position)

            # If player 2 wins the game
            if win_check(xoBoard, player2_marker):
                display_board(xoBoard)
                print('Congratulations!!!! You have won the game!!! You win a $25 gift card to Starbucks!!!')
                game_begins = False
            else:
                if full_board_check(xoBoard):
                    display_board(xoBoard)
                    print("It's a Draw!!!!")
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break