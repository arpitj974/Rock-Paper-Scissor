import random
from constants import Action


class Computer:
    wins = 0
    actions = []
    last_action = None

    def get_wins(self):
        return self.wins

    def get_last_action(self):
        return self.last_action

    def get_action(self):
        """
        Get computer action

        :return: integer representing computer action
        """
        computer_action = random.choice([member.value for member in Action])
        self.actions.append(computer_action)
        self.last_action = computer_action
        return computer_action

    def win(self):
        self.wins += 1
