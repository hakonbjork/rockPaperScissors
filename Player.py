from Action import Action

""" Player class """

class Player():
    """ Basic class Player to have methods for all players """

    def __init__(self):
        self.action = None
        self.name = None
        self.actions = [Action("rock"), Action("paper"), Action("scissor")]
        self.op_actions = [] # opponent's choice of action in each game
        self.results = [] # points gotten in each game
        self.current_win_rates = []

    def receive_result(self, op_action, points_received):
        """ receiving and saving results from one game """

        # Function receives action of opponent, and points earned
        # These two will be saved in separate lists for later
        self.op_actions.append(op_action)
        self.results.append(points_received)

    def enter_name(self, name):
        """ Method to save a name for the player instance """
        self.name = name

    def __str__(self):
        """ define what str() should print in player object"""
        return self.name
