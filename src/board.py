import tetrimino

class Board:

    # Constructor
    def __init__(self, width, height, borderChar, innerChar, state=""):
        self.width = width
        self.height = height
        self.borderChar = borderChar
        self.innerChar = innerChar
        self.activeTetrimino = None
        self.inactiveTetriminos = None
        
        # Checking if the state has been instantiated
        if state == "":
            self.createEmptyBoard()
        else:
            self.state = state

    """
    # Create an empty board for the start of the game
    def createEmptyBoard(self):
        # Creating borders for the floor and ceiling
        horizontalWall = self.borderChar * (self.width + 2) + '\n'

        # Creating borders for the side walls
        verticalSlice = self.borderChar + ('  ' * self.width) + self.borderChar + '\n'
        verticalWalls = verticalSlice * self.height
        
        return horizontalWall + verticalWalls + horizontalWall
    """

    def createEmptyBoard(self):
        boardState = []

        horizontalRow = []
        for x in range(self.width + 2):
            horizontalRow.append(self.borderChar)
        

        boardState.append(horizontalRow)

        for x in range(self.height):
            verticalRow = []
            verticalRow.append(self.borderChar)
            for x in range(self.width):
                verticalRow.append(self.innerChar)
            verticalRow.append(self.borderChar)
            boardState.append(verticalRow)

        boardState.append(horizontalRow)

        self.state = boardState

    # Prints the current state of the board to the terminal
    def printState(self):
        rowsToOmit = self.height - 20
        for index, row in enumerate(self.state):
            if index >= rowsToOmit:
                print(*row, sep="")
        
    # Creates a new tetrimino and adds it to the top left of the board
    def spawnTetrimino(self):
        self.activeTetrimino = tetrimino.Tetrimino()

        self.drawTetriminoState(1, 1, True)

    def moveDown(self):

        # Removing piece from baord's state
        self.drawTetriminoState(self.activeTetrimino.bounds[0][0], self.activeTetrimino.bounds[0][1], False)

        # Moving bounds
        for pair in self.activeTetrimino.bounds:
            pair[1] += 1

        # Redrawing state
        self.drawTetriminoState(self.activeTetrimino.bounds[0][0], self.activeTetrimino.bounds[0][1], True)

    # Draw is a boolean, being true if drawing and false if erasing
    def drawTetriminoState(self, x, y, draw):
        if draw:
            for rowIndex, row in enumerate(self.activeTetrimino.state):
                for columnIndex, char in enumerate(row):
                    self.state[rowIndex + y][columnIndex + x] = char
        else:
            for rowIndex, row in enumerate(self.activeTetrimino.state):
                for columnIndex, char in enumerate(row):
                    self.state[rowIndex + y][columnIndex + x] = self.innerChar
                    


