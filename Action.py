""" class to represent action selected """


class Action():
    """ class to represent action selected """

    def __init__(self, move):
        self.move = move
        if move not in ["rock", "paper", "scissor"]:
            print("Error: Bad movement name: " + str(self.move))

    def __str__(self):
        """ define what str() should print in acion object"""
        return self.move

    def __eq__(self, other):
        """ define when it is equal """
        return self.move == other.move

    def __gt__(self, other):
        """ define what move is the best """
        if self.move == "rock":
            return other.move == "scissor"
        if self.move == "paper":
            return other.move == "rock"
        if self.move == "scissor":
            return other.move == "paper"

