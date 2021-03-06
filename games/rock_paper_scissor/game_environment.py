import sys
from games.game_environment_general import GameEnvironmentGeneral
from games.rock_paper_scissor.contestant_template import Action
from games.rock_paper_scissor.config import ITERATIONS, NUM_PLAYERS, TURN_BASED, WIN_CRITERIA

class GameEnvironment(GameEnvironmentGeneral):
    def __init__(self, suspense):
        super().__init__(ITERATIONS, NUM_PLAYERS, TURN_BASED, WIN_CRITERIA, suspense)

    def get_reward(self, moves:dict, game_board=None):
        ''' Calculate the score of each player
        :param moves: A dictionary with keys that equal the player name and a value
                      that is one of the possible Actions.
                      E.g: {'player1_name': Action1, 'player2_name': Action2}
        '''
        players = list(moves.keys())
        actions = [moves[player] for player in players]

        # Sanity-check on player actions
        assert actions[0] in Action
        assert actions[1] in Action
        
        # DRAW
        if actions[0] == actions[1]:
            rewards = [0, 0]
            winner = None
            print("X", end='')

        # PLAYER 0 WINS
        elif (actions[0] == Action.ROCK and actions[1] == Action.SCISSOR) \
            or (actions[0] == Action.PAPER and actions[1] == Action.ROCK) \
            or (actions[0] == Action.SCISSOR and actions[1] == Action.PAPER):
            rewards = [1, 0]
            winner = players[0]
            print("<", end='')
        
        # PLAYER 1 WINS
        elif (actions[0] == Action.ROCK and actions[1] == Action.PAPER) \
            or (actions[0] == Action.PAPER and actions[1] == Action.SCISSOR) \
            or (actions[0] == Action.SCISSOR and actions[1] == Action.ROCK):
            rewards = [0, 1]
            winner = players[1]
            print(">", end='')

        self.game_over = True
        sys.stdout.flush()  # Forces the buffer to be written to stdout

        return {
            'winner': winner,
            'players': {
                players[0]: {
                    'action': actions[0],
                    'reward': rewards[0]
                },
                players[1]: {
                    'action': actions[1],
                    'reward': rewards[1]
                }
            }
        }

    def get_game_board(self, players, iteration:int):
        return None