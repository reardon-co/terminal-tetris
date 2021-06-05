import blessed
import board
import tetrimino
import collections
import copy

term = blessed.Terminal()
gameBoard = board.Board(10, 20, '⬜', '⬛')
piece = tetrimino.Tetrimino()

# Main game loop
# - Check if the state of the board changed
# - Update the display of the state
# - Make changes if needed
# - Repeat

def gameLoop():
    currBoardState = [[]]
    
    # Checking board state and updating
    while True:
        if not sorted(gameBoard.state) == sorted(currBoardState):
            gameBoard.printState()
            currBoardState = copy.deepcopy(gameBoard.state)
    
    # Changing board state
        


gameLoop()
