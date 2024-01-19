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

    
