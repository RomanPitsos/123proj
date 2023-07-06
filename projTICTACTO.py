#board/variables
board=["-", "-" , "-",
       "-", "-", "-",
       "-", "-", "-"]

winner= None

current_player="X"

def gameBoard(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])


#playerinput


def player_input(board):
    while True:

        input_p=int(input("Enter your choise number 1-9:"))
        if input_p>=1 and input_p<=9 and board[input_p-1]=="-":
            board[input_p-1]=current_player
            break
            
    
        else:   print("Please choose from 1-9:")
        

# check win/tie

def checkRow(board):
    global winner
    if (board[0]==board[1]==board[2] and board[0]!="-") or (board[3]==board[4]==board[5] 
        and board[3]!="-") or (board[6]==board[7]==board[8] and board[6]!="-"):
        
        return True   
    
def checkLine(board):
    global winner
    if (board[0]==board[3]==board[6] and board[0]!="-") or (board[1]==board[4]==board[7] 
        and board[1]!="-") or (board[2]==board[5]==board[8] and board[2]!="-"):
        
        return True  
    
def checkDiag(board):
    
    if (board[0]==board[4]==board[8] and board[0]!="-") or (board[2]==board[4]==board[6] 
        and board[2]!="-"):
        
        return True   
    
def checkTie(board):   
    
    if "-" not in board:

        gameBoard(board)
        print("It's a tie!")
        return True

def checkWin():
    global winner
    if checkDiag(board) or checkLine(board) or checkRow(board):
        winner=current_player
        return True



#switch players

def switch_players():
    global current_player
    if current_player=="X":
        current_player="O"
    else:
        current_player="X"


#game
game = True
while game:
    gameBoard(board)
    player_input(board)
    if checkWin():
        gameBoard(board)
        print(f'The winner is {winner}!')
        break
    if checkTie(board):
        break
    switch_players()

