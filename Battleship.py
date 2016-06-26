from random import randint

# ####
# Battleship
# ####
# A simple text-based Battleship game using for loops and functions
# Completed and tweaked by Anthony Lee
# from Unit7: List and Functions: "Battleship!" on Codecademy

# Initial setup
board = []
shiplocation = "My ship is at "
# turnnumber = turn

# Build play board
for x in range(5):
    board.append(["O"] * 5)

# Function: print current playboard iteration
def print_board(board):
    for row in board:
        print " ".join(row)

# Initial start game print statements
print "\nLet's play Battleship!\n"
print "You have 5 chances"
print_board(board)

# Define random ship coordinates
def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

# Debugging data
print ship_row
print ship_col

# Loop game for turn by turn basis
# Note to self: Keep for loop at turn + 1 times b/c range is exclusive
# In turn check conditions to break, notice turn starts at turn + 1
# hence, turn check should be turn - 1 times
for turn in range(5):
    print "\nTurn", turn + 1
    
    #Catch error
    try:
        guess_row = int(raw_input("Guess Row: "))
        guess_col = int(raw_input("Guess Col: "))
    # except EOFError:
    #     # print ("Error: EOF or empty input!")
    #     # guess_row = " "  
    #     # guess_col = " "
    #     # continue
    except ValueError:
        print ("Error: Not an integer")
        guess_row = " "
        guess_col = " "
        continue
    # print guess_row
    # print guess_col

    #if guess is correct
    if guess_row == ship_row and guess_col == ship_col:
        # print " "
        print "\nCongratulations! You sunk my battleship!"
        board[guess_row][guess_col] = "X"
        print_board(board)
        break
        
    else:
        # If guess input is not within ocean
        # Do not forget to change the bounds check if playboard size changes
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "\nOops, that's not even in the ocean.\n"
            
            if turn == 4:
                print "Game Over"
                print_board(board)
                print " "
                print shiplocation, ship_row, ship_col
                break
            
        #If guess input is already used    
        elif(board[guess_row][guess_col] == "X"):
            print "\nYou guessed that one already.\n"
        
            if turn == 4:
                print "Game Over"
                print_board(board)
                print " "
                print shiplocation, ship_row, ship_col
                break
                    
        #Miss battleship condition    
        else:
            # print " "
            print "\nYou missed my battleship!\n"
            # print " "
            board[guess_row][guess_col] = "X"
            
            if turn == 4:
                print "Game Over"
                print_board(board)
                print " "
                print shiplocation, ship_row, ship_col
                break
            
        #Print out board after each turn regardless of condition
        print_board(board)
