""" MostCommon player class """

import random
from Player import Player

class MostCommon(Player):
    """ MostCommon Player class """

    def select_action(self):
        """ selects action based on opponent's most played action """

        # error message for testing
        if len(self.op_actions) < 1:
            r = random.randint(0, 2)
            self.action = self.actions[r]
            # print("Hmmm, little common to know...")
            return

        # finds most common action of opponen from op_actions list
        # and choses the winning action against that action
        most_common = max(self.actions, key=self.op_actions.count)
        index = self.actions.index(most_common)
        self.action = self.actions[(index + 1) % 3]
