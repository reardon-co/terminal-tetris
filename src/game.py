import blessed
import board
import tetrimino
import collections
import copy
from functools import reduce
from time import sleep

term = blessed.Terminal()
gameBoard = board.Board(10, 20, '⬜', '⬛')
piece = tetrimino.Tetrimino()
fps = 60

# Main game loop
# - Check if the state of the board changed
# - Update the display of the state
# - Make changes if needed
# - Repeat

def updateState():
    handleFallingTetrimino()


def handleFallingTetrimino():
    sleep(0.5)
    if gameBoard.activeTetrimino is None:
        gameBoard.spawnTetrimino()
    elif gameBoard.isTileBelowSafe():
        gameBoard.moveDown()
    
def areStatesEqual(state):
    return reduce.reduce(lambda i, j : i and j, map(lambda m, k: m == k, gameBoard.state, state), True)


def gameLoop():
    currBoardState = [[]]
    
    # Checking board state and updating
    while True:
        sleep(1/fps)
        if not reduce(lambda i, j : i and j, map(lambda m, k: m == k, gameBoard.state, currBoardState), True):
            print(term.clear + term.home)
            gameBoard.printState()
            currBoardState = copy.deepcopy(gameBoard.state)
    
    # Changing board state
        updateState()


gameLoop()
