""" module docstring """

from Player import Player
from Random import Random
from Sequential import Sequential


class SingleGame():
    """ docstring """

    def __init__(self, player1, player2):
        """ docstring """
        self.player1 = player1
        self.player2 = player2
        self.result_text = None

    def perform_game(self):
        """ get choice from players, determine result, report back """
        
        self.player1.select_action()
        self.player2.select_action()
        # print("Action chosen! Time to fight!")
    
        p1_move = self.player1.action
        p2_move = self.player2.action

        if p1_move == p2_move:  # draw, 1/2 points to each
            self.player1.receive_result(p2_move, 0.5)
            self.player2.receive_result(p1_move, 0.5)
            self.result_text = "Game was a draw."

        elif p1_move > p2_move:  # player1 wins
            self.player1.receive_result(p2_move, 1)
            self.player2.receive_result(p1_move, 0)
            self.result_text = f"{self.player1.name} wins!"

        else:  # player2 wins
            self.player1.receive_result(p2_move, 0)
            self.player2.receive_result(p1_move, 1)
            self.result_text = f"{self.player2.name} wins!"

        # Append current win rate to list of current win rates
        p1_current_win_rate = sum(self.player1.results)/len(self.player1.results)
        p2_current_win_rate = sum(self.player2.results)/len(self.player2.results)
        self.player1.current_win_rates.append(p1_current_win_rate)
        self.player2.current_win_rates.append(p2_current_win_rate)

    def show_result(self):
        """ Shows a textual representation of the results """
        p1_action = self.player1.action
        p2_action = self.player2.action
        setence = f"{self.player1.name}: {p1_action}, {self.player2.name}: {p2_action} --> {self.result_text}"

        print(setence)


def test():
    """ Testing stuff to see it works properly """
    a = Random()
    b = Sequential()
    a.enter_name("Player Random")
    b.enter_name("Player Sequential")

    game = SingleGame(a, b)
    game.perform_game()
    game.show_result()

if __name__ == "__main__":
    test()