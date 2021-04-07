""" Module for Random Player class """

from random import randint
from Player import Player

class Random(Player):
    """ Random Player class"""

    def select_action(self):
        """ Selects a random action """
        num = randint(0, 2)
        self.action = self.actions[num]
