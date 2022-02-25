from methodology.constants import ConstantValues

class Winner:

    def __init__(self):
        self.constants = ConstantValues()

    def check_sublist(self, list1):
        output = False
        counter = 0
        for i in range(0, len(self.constants.list_winning_positions)):
            for j in range(0, len(list1)):
                if (list1[j] in self.constants.list_winning_positions[i]):
                    counter += 1
                    if (counter == 3):
                        output = True
                        break
            counter = 0
        return output

    def check_winner(self, list_player_positions, list_cpu_positions):
        # need here a global value in which we store the response in order to check the loop when adding
        response_player = self.check_sublist(list_player_positions)
        response_cpu = self.check_sublist(list_cpu_positions)
        response = " "
        for list_winner in self.constants.list_winning_positions:
            # here we need to make all cases of draw/winning
            if (len(list_player_positions) + len(list_cpu_positions) == 9) and response_player:
                response = "You snatch it. You won at the final turn"
                break

            elif (len(list_player_positions) + len(list_cpu_positions) == 9) and response_cpu:
                response = "Computer has won at the last turn"
                break

            elif (len(list_player_positions) + len(list_cpu_positions) == 9):
                response = "It is a draw"

            #check what is  the value of check_sublist for every list
            elif response_player and len(list_player_positions)<5:
                response = "You have won"
                break
            elif response_cpu and len(list_cpu_positions)<5:
                response="Computer has won"
                break
        return response





