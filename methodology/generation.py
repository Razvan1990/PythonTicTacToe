import random
from methodology.constants import ConstantValues
class GeneratorThings:

    def __init__(self):
        self.constants = ConstantValues()

    def generate_number_cpu(self):
        x = random.randint(1, 9)
        return x

    def generate_starter(self):
        x = random.randint(1,2)
        return x

    def player_choose_position(self):
        x = int(input("Choose a valid  position "))
        while x<1 or x>9:
            print("Not a correct position on the table. Insert a correct position")
            x = int(input(" "))
        return x

    '''
    @list_taken_positions will be an empty list defined as a global variable and will append each time the function is called
    '''
    def insert_piece_on_table(self, playerName, chosenPosition, list_taken_positions):
        symbol =" "
        if playerName not in self.constants.dict_characters.keys():
            raise Exception("Not a correct player name")
        if playerName=="player":
            symbol = self.constants.dict_characters[playerName]
        elif playerName == "cpu":
            symbol = self.constants.dict_characters[playerName]

        #this will be done by generating all positions in a compute function
        #by introducing all numbers in list we then could simply see if the position is valid for input or not
        if chosenPosition==1:
            self.constants.board[0][0]=symbol
            list_taken_positions.append(1)
        elif chosenPosition==2:
            self.constants.board[0][2]=symbol
            list_taken_positions.append(2)
        elif chosenPosition==3:
            self.constants.board[0][4]=symbol
            list_taken_positions.append(3)
        elif chosenPosition == 4:
            self.constants.board[2][0] = symbol
            list_taken_positions.append(4)
        elif chosenPosition==5:
            self.constants.board[2][2]=symbol
            list_taken_positions.append(5)
        elif chosenPosition==6:
            self.constants.board[2][4]=symbol
            list_taken_positions.append(6)
        elif chosenPosition==7:
            self.constants.board[4][0]=symbol
            list_taken_positions.append(7)
        elif chosenPosition==8:
            self.constants.board[4][2]=symbol
            list_taken_positions.append(8)
        elif chosenPosition==9:
            self.constants.board[4][4]=symbol
            list_taken_positions.append(9)






