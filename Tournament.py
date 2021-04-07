""" module for the Tournament class """

import matplotlib.pyplot as plot
from SingleGame import SingleGame
from MostCommon import MostCommon
from Sequential import Sequential
from Random import Random
from Historian import Historian

class Tournament():
    """ Class for setting up multiple games """

    def __init__(self, player1, player2, number_of_games):
        """ sets up instance with two players and number of games
        to be played """

        self.p1 = player1
        self.p2 = player2
        self.num = number_of_games

    def arrange_singlegame(self):
        """ Play out a single game, report results """

        game = SingleGame(self.p1, self.p2)
        game.perform_game()
        # can show result as well if wanted:
        game.show_result()

    def arrange_tournament(self):
        """ Play out the number of games """

        # play the games
        for i in range(self.num):
            self.arrange_singlegame()
        
        p1_win_percentage = sum(self.p1.results)/len(self.p1.results)
        p2_win_percentage = sum(self.p2.results)/len(self.p2.results)
        print(f"{self.p1.name} win percentage: {p1_win_percentage}")
        print(f"{self.p2.name} win percentage: {p2_win_percentage}")

        # Plot result with focus to player 1
        while True:
            show_plot = input("Do you want to show plot? Y/N: ")
            if show_plot not in ["Y", "N"]:
                continue
            break
        if show_plot == "Y":
            plot.plot(self.p1.current_win_rates)
            plot.ylabel = f"Win rate for {self.p1}"
            plot.show()
        
        end_message = input("Thanks for playing. Press ENTER to quit ")

def welcome_message():
    """ Prints a welcome message for textual interface """

    message1 = "Time to choose player! Enter \"H\" for  Historian, "
    message2 = "\"MC\" for MostCommon, \"S\" for Sequential "
    print("Welcome to rock, scissor, paper!")
    print("--------------------------------")
    print(message1 + message2 + "and \"R\" for Random!" )

def choose_players():
    """ Let user choose players and player names in textual interface"""

    # Available picks
    player_type_list = ["H", "MC", "S", "R"]
    players = []
    while len(players) < 2: # Until the player count is two
        i = len(players) + 1 # Number of current player
        while True:
            player_type_input = input(f"Player {i}: ")

            if player_type_input not in player_type_list:
                print("Invalid input! Please try again.")
                continue # Loop will continue until valid input
        
            break

        if player_type_input == "H":
            while True:
                try:
                    memo = int(input("What will memory of Historian be? "))
                except:
                    continue
                if 1 <= memo <= 20:
                    break
            player = Historian(memo)
        
        if player_type_input == "MC":
            player = MostCommon()
        if player_type_input == "S":
            player = Sequential()
        if player_type_input == "R":
            player = Random()
        
        player_name = input("Player name: ")
        player.enter_name(player_name)
        
        players.append(player)
        i += 1

    return players # List with players to enter tournament

def create_tournament(players):
    """ Asks for number of games, creates instance of tournament class 
    with players and number og games to be played """
    
    while True:
        try:
            num_games = int(input("How many games? "))
        except:
            continue
        if 1 <= num_games <= 100000:
            break
    tournament = Tournament(players[0], players[1], num_games)
    print("Let the games begin!")
    tournament.arrange_tournament()

def main():
    """ Main funksjon for file. Text-interface tournament """

    welcome_message()
    players = choose_players()
    create_tournament(players)
    
def test():
    """ Test to check that things work properly """

    mc = MostCommon()
    hi = Historian(2)
    mc.enter_name("Most Common")
    hi.enter_name("Historian")
    tournament = Tournament(mc, hi, 100)
    tournament.arrange_tournament()


if __name__ == "__main__":
    main()
