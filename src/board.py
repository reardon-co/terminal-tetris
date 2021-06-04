class Board:

    # Constructor
    def __init__(self, width, height, borderChar, state=""):
        self.width = width
        self.height = height
        self.borderChar = borderChar
        
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
        
        verticalRow = []
        verticalRow.append(self.borderChar)
        for x in range(self.width):
            verticalRow.append('  ')
        verticalRow.append(self.borderChar)

        boardState.append(horizontalRow)
        for x in range(self.height):
            boardState.append(verticalRow)
        boardState.append(horizontalRow)

        self.state = boardState

    # Prints the current state of the board to the terminal
    def printState(self):
        for row in self.state:
            print(*row, sep="")
