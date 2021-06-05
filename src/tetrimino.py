import random

class Tetrimino:
    def __init__(self):
        self.type = random.choice(['I', 'O', 'S', 'Z', 'J', 'L', 'T'])
        self.state = self.typeState()
        self.width = len(self.state[0])
        self.height = len(self.state)
        self.bounds = self.initializeBounds() # x,y coordinates in order UL, UR, LR, LL

    def typeState(self):
        cyanI = [['🟫','🟫','🟫','🟫']]
        yellowO = [['🟨','🟨'],['🟨','🟨']]
        greenS = [['⬛','🟩','🟩'],['🟩','🟩','⬛']]
        redZ = [['🟥','🟥','⬛'],['⬛','🟥','🟥']]
        blueJ = [['🟦','⬛','⬛'],['🟦','🟦','🟦']]
        orangeL = [['⬛','⬛','🟧'],['🟧','🟧','🟧']]
        purpleT = [['⬛','🟪','⬛'],['🟪','🟪','🟪']]

        switcher= {
            'I': cyanI,
            'O': yellowO,
            'S': greenS,
            'Z': redZ,
            'J': blueJ,
            'L': orangeL,
            'T': purpleT
        }

        return switcher.get(self.type)
    
    # Rotates the tetrimino clockwise by 90 degrees
    def rotate(self):
        newState = []

        for i in range(self.width):
            rotatedRow = []
            for row in self.state:
                rotatedRow.insert(0,row[i])
            newState.append(rotatedRow)
            
        self.state = newState

        self.bounds.insert(0, self.bounds.pop())

    # Prints the current state to the terminal
    def printState(self):
        for row in self.state:
            print(*row, sep="")

    # Sets the intial bounds of the tetrimino
    def initializeBounds(self):
        switcher= {
            'I': [[1, 1], [4, 1], [4, 1], [1, 1]],
            'O': [[1, 1], [2, 1], [2, 2], [1, 2]],
            'S': [[1, 1], [3, 1], [3, 2], [1, 2]],
            'Z': [[1, 1], [3, 1], [3, 2], [1, 2]],
            'J': [[1, 1], [3, 1], [3, 2], [1, 2]],
            'L': [[1, 1], [3, 1], [3, 2], [1, 2]],
            'T': [[1, 1], [3, 1], [3, 2], [1, 2]]
        }

        return switcher.get(self.type)