from blessed import Terminal
import blessed
import board

term = blessed.Terminal()


board = board.Board(10, 20, '⬜')
board.printState()