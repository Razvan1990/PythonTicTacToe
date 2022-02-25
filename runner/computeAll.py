from datetime import datetime
import time
import timedelta

from methodology.printBoard import PrintBoard
from methodology.winner import Winner
from methodology.generation import GeneratorThings

class Computation:

    def __init__(self):
        self.printer = PrintBoard()
        self.winner = Winner()
        self.gen = GeneratorThings()

    def computeMethod(self):

        #see first who starts the game

        player_start = self.gen.generate_starter()

        #list for player and cpu
        player_list =[]
        cpu_list =[]


        print("TicTacToe game in python")
        original_date = datetime.now()
        self.printer.displayBoard()



        if player_start==1:
            print("You will start the game")
            time.sleep(0.5)
            while True:
                player_pos = self.gen.player_choose_position()
                while(player_pos in player_list or player_pos  in cpu_list ):
                    print("Position is already taken. Please choose again")
                    player_pos = self.gen.player_choose_position()
                #put symbol on the table
                self.gen.insert_piece_on_table("player",player_pos,player_list)
                #need to print board here
                print("Updated board")
                self.printer.displayBoard()
                #check now to see if we have a winner
                check_winner= self.winner.check_winner(player_list, cpu_list)
                if(check_winner!=" "):
                    print(check_winner)
                    break
                #now it is the turn for the cpu
                cpu_pos = self.gen.generate_number_cpu()
                while(cpu_pos in player_list or cpu_pos in cpu_list):
                    print("Regenerating valid position")
                    cpu_pos = self.gen.generate_number_cpu()
                #insert cpu position
                self.gen.insert_piece_on_table("cpu",cpu_pos,cpu_list)
                print("Updated board")
                self.printer.displayBoard()
                #check again to see if we have a winner
                check_winner = self.winner.check_winner(player_list, cpu_list)
                if(check_winner!=" "):
                    print(check_winner)
                    break

        if player_start == 2:
            print("Computer will start the game")
            time.sleep(0.5)
            while True:
                cpu_pos = self.gen.generate_number_cpu()
                while (cpu_pos in player_list or cpu_pos in cpu_list):
                    print("Regenerating valid position")
                    cpu_pos = self.gen.generate_number_cpu()
                # put symbol on the table
                self.gen.insert_piece_on_table("cpu", cpu_pos, cpu_list)
                print("Updated board")
                self.printer.displayBoard()
                # check now to see if we have a winner
                check_winner = self.winner.check_winner(player_list, cpu_list)
                if (check_winner != " "):
                    print(check_winner)
                    break
                # now it is the turn for the cpu
                player_pos = self.gen.player_choose_position()
                while (player_pos in player_list or player_pos in cpu_list):
                    print("Position is already taken. Please choose again")
                    player_pos = self.gen.player_choose_position()
                # insert cpu position
                self.gen.insert_piece_on_table("player", player_pos, player_list)
                print("Updated board")
                self.printer.displayBoard()
                # check again to see if we have a winner
                check_winner = self.winner.check_winner(player_list, cpu_list)
                if (check_winner != " "):
                    print(check_winner)
                    break

        final_datetime = datetime.now()

        match_duration = final_datetime-original_date

        print("Game duration in seconds", "%.2f" %match_duration.total_seconds())







