import sys

PLAYER_1_PITS = ('A', 'B', 'C', 'D', 'E', 'F')
PLAYER_2_PITS = ('G', 'H', 'I', 'J', 'K', 'L')

OPPOSITE_PIT = {'A': 'G', 'B': 'H', 'C': 'I', 'D': 'J', 'E': 'K','F': 'L', 'G': 'A', 'H': 'B', 'I': 'C', 'J': 'D', 'K': 'E', 'L': 'F'}
NEXT_PIT = {'A':'B', 'B': 'C', 'C':'D', 'D':'E', 'E':'F', 'F':'1', '1':'L', 'L':'K', 'K': 'J', 'J':'I', 'I':'H', 'H':'G', 'G':'2', '2':'A'}

PIT_LABELS = 'ABCDEF1KJIHG2'

STARTING_NUMBERS_OF_SEEDS = 4

def main():
    print('manacala by invent with python')
    input ('press enter to begin...')

    gameBoard = getNewBoard()
    playerTurn = '1'

    while True:
        print('\n' * 60)
        displayBoard(gameBoard)
        playerMove = askForPlayerMove(playerTurn, gameBoard)
        playerTurn = makeMove(gameBoard, playerTurn, playerMove)

        winner = checkforWinner(gameBoard)
        if winner == '1' or winner == '2':
            displayBoard(gameBoard)
            print('Player' + winner + 'has won!')
            sys.exit()
        elif winner == 'tie':
            displayBoard(gameBoard)
            print('there is a tie!')
            sys.exit
        
def getNewBoard():
    s = STARTING_NUMBERS_OF_SEEDS
    return {'1':0, '2':0, 'A': s, 'B': s, 'C': s, 'D': s, 'E': s, "F": s, 'G': s, 'H': s, 'I': s, 'J': s, 'K': s, 'L': s }

def displayBoard(board):
    seedAmounts = []
    for pit in 'GHIJKL21ABCDEF':
        numSeedsInThisPit = str(board[pit]).rjust(2)
        seedAmounts.append(numSeedsInThisPit)

        print("""
        +------+------+--<<<<<-Player 2---+------+------+-----+
        2.      |G     |H.     |I.     |J      |K.       |L.   |  1
                |      |       |.      |       |         |.    |.  
        S.      |  { } |  { }  |. { }  | { }   | { }     |  { }|.  S
        T.      |.     |.      |       |.      |.        |     |   T
        O. { }. +------+-------+-------+-------+---------+-----+.{}O
        R.      |A.    |B.     |C.     |D.     |E.       | F.  |.  R
        E.      |  { } |  { }  |. { }  |  { }. |  { }    | { } |   E
        +-------+------+------PLAYER 1->>>>----+---------+-----+----+
        """.format(*seedAmounts)) 

def askForPlayerMove(playerTurn, board):
    while True:
        if playerTurn == '1':
            print('Player 1, choose move: A-F (or QUIT)')
        elif playerTurn =='2':
            print('Player 2, choose move G- L(or QUIT)')
        response input('> ').upper().strip()
        
        if response == 'QUIT':
            print('THanks for playing')
            sys.exit
        

