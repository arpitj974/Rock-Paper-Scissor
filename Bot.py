import random
from constants import Action


class Computer:
    """
    This class has all the methods and attributes needed to represent the machine as a player
    """
    __wins = 0
    __actions = []          # Records all the actions chosen by the computer in this session
    __last_action = None    # Records the last action chosen by the computer

    def get_wins(self):
        return self.__wins

    def get_last_action(self):
        return self.__last_action

    def get_action(self):
        """
        Get computer action

        :return: integer representing computer action
        """
        computer_action = random.choice([member.value for member in Action])
        self.__actions.append(computer_action)
        self.__last_action = computer_action
        return computer_action

    def win(self):
        self.__wins += 1
