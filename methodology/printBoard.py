from methodology.constants import ConstantValues
class PrintBoard:

    def __init__(self):
        self.constants = ConstantValues()
        
    def displayBoard(self):
        for i in range(0, len(self.constants.board)):
            for j in range(0, len(self.constants.board)):
                print(self.constants.board[i][j], end=" ")
            print()

    
    