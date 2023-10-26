from player import Player
a = False
menu = """
 _______________________
|C  |O  |N  |N  |E  |C T|
-------------------------
|   |X  |   |X  |   |   |
-------------------------
|   |x  |   |O  |   |   |
-------------------------
|   |O  |x  |O  |   |   |
-------------------------
|   |   |   |O  |   |   |
-------------------------
|   |   |   |x  |   |   |
-------------------------
||                     ||
/\                     /\ 
"""

print(menu)
gam = input("TYPE START TO START! OR TYPE HELP FOR INSTRUCTIONS \n")
def game():

    b = """
      1   2   3   4   5   6
     _______________________
    |   |   |   |   |   |   |
    -------------------------
    |   |   |   |   |   |   |
    -------------------------
    |   |   |   |   |   |   |
    -------------------------
    |   |   |   |   |   |   |
    -------------------------
    |   |   |   |   |   |   |
    -------------------------
    |   |   |   |   |   |   |
    -------------------------
    ||                     ||
    /\                     /\ 
    """

    board = [[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "]]

    def printBoard(board,symbol,player1,player2):    
        print(" "*2 + "1" +" "*3 + "2" + " "*3 + "3" +" "*3 + "4" + " "*3 + "5" +" "*3 + "6") 
        print(" "+"_"*23)
        for r in range(6):
            print("|"+board[r][0] + "  |" + board[r][1] + "  |" + board[r][2] + "  |" + board[r][3] + "  |" + board[r][4] + "  |" + board[r][5] + "  |")
            if r<5:
                print("-"*25)
        print("-"*25)
        print("||" + " "*21 + "||" )
        print("/\ " + " "*20 + "/\ " )
        if symbol == "X":
            print(f"{player1}: YOUR TURN")
        elif symbol == "O":
            print(f"{player2}: YOUR TURN")
        else:
            print("")

    def chooseSpot(r,c,symbol,board):
        #if the spot is open
        for i in range(6):
            if board[r][c] == " ":
                #add the symbol and return true
                board[r][c]=symbol
                return True
            r -= 1
        return False

    def catGame(board):
        #check every spot to see if there is something
        for row in range(len(board)):    #range(len(sampleBoard))->[0,1,2]
                for columns in range(len(board[row])):
                    if (board[row][columns]) == " ":
                       return False
        printBoard(board,symbol,player1,player2)
        print("TIE!")
        return True   

    def checkForWinners(board):
             #check horizontally
            for r in range(len(board)):
                for c in range(len(board)):
                    #r is the rows and the columns are the same for each row
                    if (board[r][c] == board[r][c-1] and board[r][c-1] == board[r][c-2] and board[r][c-2] == board[r][c-3]) and board[r][c]!=" ":
                        print(f"Winner winner Turkey breakfeast! {symbol}!")
                        printBoard(board,"Q",player1,player2)
                        return True
                    
                    if c <= 2:
                        if (board[r][c] == board[r][c+1] and board[r][c+1] == board[r][c+2] and board[r][c+2] == board[r][c+3]) and board[r][c]!=" ":
                            print(f"Winner winner Turkey breakfeast! {symbol}!")
                            printBoard(board,"Q",player1,player2)
                            return True

            #check vertically
            for r in range(len(board)):
                for c in range(len(board)):
                    #r is the rows and the columns are the same for each row
                    if (board[r][c] == board[r-1][c] and board[r-1][c] == board[r-2][c] and board[r-2][c] == board[r-3][c]) and board[r][c]!=" ":
                        print(f"Winner winner Turkey breakfeast! {symbol}!")
                        printBoard(board,"Q",player1,player2)
                        return True
                
                    if r <= 2:
                        if (board[r][c] == board[r+1][c] and board[r+1][c] == board[r+2][c] and board[r+2][c] == board[r+3][c]) and board[r][c]!=" ":
                            print(f"Winner winner Turkey breakfeast! {symbol}!")
                            printBoard(board,"Q",player1,player2)
                            return True

            #check diagonally
            for r in range(len(board)):
                for c in range(len(board)):
                    # r is the rows and c is the columns
                    # diagonial bot right to top left
                    if (board[r][c] == board[r-1][c-1] and board[r-1][c-1] == board[r-2][c-2] and board[r-2][c-2] == board[r-3][c-3] and board[r][c]!=" "):
                        print(f"Winner winner Turkey breakfeast! {symbol}!")
                        printBoard(board,"Q",player1,player2)
                        return True
                    
                    if c<=2:
                        if (board[r][c] == board[r-1][c+1] and board[r-1][c+1] == board[r-2][c+2] and board[r-2][c+2] == board[r-3][c+3] and board[r][c]!=" "):
                            print(f"Winner winner Turkey breakfeast! {symbol}!")
                            printBoard(board,"Q",player1,player2)
                            return True
                    
                    if r <= 2 and c <= 2:                    
                        if (board[r][c] == board[r+1][c+1] and board[r+1][c+1] == board[r+2][c+2] and board[r+2][c+2] == board[r+3][c+3] and board[r][c]!=" "):
                            print(f"Winner winner Turkey breakdeast! {symbol}!")
                            printBoard(board,"Q",player1,player2)
                            return True
                    
                    

    symbol = "X"
    id = 1
    player1 = Player(input("Name: "),symbol,id)
    id += 1
    player2 = Player(input("Name: "),symbol="O",id=id)
    
    while symbol != "Q":

        printBoard(board,symbol,player1,player2)
        goodSpot=False
        while not goodSpot:
            r = 5
            a = False
            while a == False:
                try:
                    c = int(input("spot: "))-1
                    a = True
                except ValueError:
                    a= False
            #if we can NOT choose the spot
            if (0<=c<=5):
                if (not chooseSpot(r,c,symbol,board)):
                    print("Invalid Spot")
                else:
                    goodSpot = True
            else:
                 print("invalid spot")
        if symbol=="X":
            symbol="O"
        elif symbol=="O":
            symbol="X"

        if catGame(board) or checkForWinners(board):
            symbol="Q"
            
def help():
    b = """
      1   2   3   4   5   6
     _______________________
    |   |   |   |   |   |   |
    -------------------------
    |   |   |   |   |   |   |
    -------------------------
    |   |   |   |   |   |   |
    -------------------------
    |   |   |   |   |   |   |
    -------------------------
    |   |   |   |   |   |   |
    -------------------------
    |   |   |   |   |   |   |
    -------------------------
    ||                     ||
    /\                     /\ 
    """
    print(b)

    print("HOW TO PLAY!")
    print("1. Decide who plays first. Players will alternate turns after playing their turn. (Player 1 will be X and Player 2 will be O)")
    print("2. On your turn, type a number 1-6 to drop one of you're pieces down the selected slot")
    print("3. Play alternates until one player gets FOUR of their piece in a row. The four in a row can be horizontal, vertical, or diagonal.")
    print("")
    
    print("HOW TO WIN!")
    print("If you're the first player to get four of your checkers in a row you win the game!")
    print("")

    # https://www.fgbradleys.com/rules/Connect%20Four.pdf <--- offical instructions

while gam.upper() != "START":
    if gam.upper() == "HELP":
        help()
    gam = input("TYPE START TO START! OR TYPE HELP FOR INSTRUCTIONS \n")

game()
