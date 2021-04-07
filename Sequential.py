""" Module for the Sequential Player class """

from Player import Player
from Action import Action

class Sequential(Player):
    """ Sequential Player class """

    def __init__(self):
        """ initiates from super, and adds a counter """

        super().__init__()
        self.counter = 0

    def select_action(self):
        """ iterates through the list of actions and updates counter """

        self.action = self.actions[self.counter]
        if self.counter < 2:
            self.counter += 1
        else:
            self.counter = 0
