from logs import logger
from constants import Action


class Player:
    wins = 0
    actions = []
    last_action = None

    def get_wins(self):
        return self.wins

    def get_last_action(self):
        return self.last_action

    def validate_action(self, action):
        """
        Checks whether the player input action is valid

        :param action: input action from console
        :return: boolean for validation check
        """
        action = action.strip()

        if len(action) == 0:
            return False

        if action.isnumeric() and int(action) in [member.value for member in Action]:
            return True
        else:
            return False

    def get_action(self):
        """
        Takes player input action from console

        :return: integer representing player action

        """

        print("\nPlease provide the number for your action: ", end="")
        while True:
            player_action = input()

            valid_action = False
            try:
                valid_action = self.validate_action(player_action)
            except Exception as e:
                logger.error("Input validation failed, exception {} ".format(e))

            if valid_action:
                self.actions.append(int(player_action.strip()))
                self.last_action = int(player_action.strip())
                break
            else:
                print("\nPlease provide a valid input number for the action: ", end="")

        return int(player_action)

    def win(self):
        self.wins += 1
