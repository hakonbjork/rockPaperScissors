""" Module for the Historian Player Class """

import random
from Player import Player
from Action import Action  # only needed for testing

class Historian(Player):
    """ Historian class looks at patterns in opponents play """

    def __init__(self, remember):
        """ Initated class. remember must be a number """
        super().__init__()
        self.remember = remember
        if not isinstance(remember, int):
            print("Error: Please use a valid number")

    def select_action(self):
        """ Looks for patterns in opponents action """

        if len(self.op_actions) < 4:
            r = random.randint(0, 2)
            self.action = self.actions[r]
            # print("Hmmm, little history to know...")
            return

        num = self.remember
        # make a list (sequence) with last [remember] elements
        sequence = self.op_actions[-num:]
        actions_after_sequence = []
        # check for that sequence in op_actions
        # not found or too few: play random
        # else, make a list with elements coming after sequence

        for i in range(len(self.op_actions)-num +1):
            add_current = True
            for j in range(num):
                if sequence[j] == self.op_actions[i+j]:
                    continue
                add_current = False
                break
            if add_current and (i + num < len(self.op_actions)):
                actions_after_sequence.append(self.op_actions[i+num])

        # choose the most common element in that list
        # play the winning play against that action
        most_common = max(self.actions, key=actions_after_sequence.count)
        index = self.actions.index(most_common)
        self.action = self.actions[(index + 1) % 3]
        # print(f"Action: {self.action}")

def test():
    """ For testing only """
    r = Action("rock")
    p = Action("paper")
    s = Action("scissor")

    hp = Historian(4)
    hp.op_actions = [s, p, p, r, s, p, r, s, s, p, p, r, s, p]
    hp.select_action()
