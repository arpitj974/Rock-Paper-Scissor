from constants import Action
from Player import Player
from Computer import Computer
from logs import logger
from time import sleep


class Game:
    score = []
    number_of_games = 0
    player1 = None
    player2 = None
    victory_rules = {Action.ROCK.name: [Action.SCISSOR.name],
                     Action.PAPER.name: [Action.ROCK.name],
                     Action.SCISSOR.name: [Action.PAPER.name]}

    @staticmethod
    def display_welcome_msg():
        print("Welcome to ROCK PAPER SCISSOR game \n")

    @staticmethod
    def display_rules():
        print("Rules of the game are as follows: \n\n"
              + "Rock vs Paper->Paper wins \n"
              + "Rock vs Scissor->Rock wins \n"
              + "Paper vs Scissor->Scissor wins \n")

    @staticmethod
    def print_action_guide():
        """
        Prints number to action mapping on screen for player convenience
        """
        print("\n----------------------------------------\n")
        print("\nYou have the following choices: \n")
        for action in Action:
            print(action.value, " - ", action.name)

    def initialize(self):
        Game.display_welcome_msg()
        Game.display_rules()  # private member
        self.player1 = Player()
        self.player2 = Computer()


    def play_again(self):
        """
        Checks whether player wants to continue playing

        :return: boolean result
        """

        result = False

        while True:
            print("\nDo you want to play again ? (y/n) ", end="")

            cont_playing = input()
            cont_playing = cont_playing.strip()

            if len(cont_playing) != 0 and cont_playing.lower() == "y":
                result = True
                break
            elif len(cont_playing) != 0 and cont_playing.lower() == "n":
                result = False
                break
            else:
                print("\nPlease provide a valid input (either y or n) :", end="")
                continue

        return result

    def get_result(self, player_action, computer_action):
        """
        Calculates and display result

        :param player_action: integer representing player action
        :param computer_action: integer representing computer action
        :return: string telling which of the following won (player or computer or draw)
        """
        player_action_name = Action(player_action).name
        computer_action_name = Action(computer_action).name

        print(player_action_name, " vs ", computer_action_name)

        result = None

        if player_action_name == computer_action_name:
            result = "draw"
            print("it's a draw")
        elif computer_action_name in self.victory_rules[player_action_name]:
            result = "player"
            print("You WIN")
            self.player1.win()
        else:
            result = "computer"
            print("Computer WINS")
            self.player2.win()

        return result


    def ask_to_start_game(self):
        print("\nPress y to start the game or press n to exit:", end="")
        result = False
        while True:
            start_game = input()
            start_game = start_game.strip()

            if len(start_game) != 0 and start_game.lower() == "y":
                result = True
                break
            elif len(start_game) != 0 and start_game.lower() == "n":
                result = False
                break
            else:
                print("\nPlease provide a valid input (either y or n): ", end="")

        return result

    def play(self):
        # session start
        logger.info("session started")
        keep_playing = self.ask_to_start_game()

        while keep_playing:
            # game start
            self.number_of_games += 1
            logger.info("Game %d" % self.number_of_games + " started")

            Game.print_action_guide()
            player1_action = self.player1.get_action()
            print("\nPlayer action : %s" % Action(player1_action).name)
            logger.debug("player action : " + Action(player1_action).name)

            sleep(1)

            print("\nNow its computer's turn....\n")

            sleep(1)

            player2_action = self.player2.get_action()
            print("\nComputer action : %s\n" % Action(player2_action).name)
            logger.debug("computer action : " + Action(player2_action).name)

            sleep(1)

            result = self.get_result(player1_action, player2_action)
            self.score.append(result)

            if result == "player" or result == "computer":
                logger.info("%s won the game" % result)
            else:
                logger.info("Game was draw")

            keep_playing = self.play_again()

        self.exit_game()

    def exit_game(self):
        if self.number_of_games > 0:
            self.display_final_session_result()

        logger.info("Session exited")
        print("\nGame finished...BYE")

    def display_final_session_result(self):
        player_wins = self.score.count("player")
        computer_wins = self.score.count("computer")
        draw_count = self.score.count("draw")

        print("\n\n==============Overall Session Results=================\n")
        print("Total games played:", self.number_of_games)
        print("Player wins :", player_wins)
        print("Computer wins :", computer_wins)
        print("Draw count:", draw_count)

        if player_wins == computer_wins:
            print("\nIt's a Draw")
        elif player_wins > computer_wins:
            print("\nYou WIN")
        else:
            print("\nComputer WINS")
