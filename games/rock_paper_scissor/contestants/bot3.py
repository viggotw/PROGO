from games.rock_paper_scissor.contestant_template import ContestantTemplate, Action

''' GAME_LOG STRUCTURE
{
    'me': {
        'score': 0,
        'moves': []
    },
    'opponents': {
        'score': [0],
        'moves': [[]]
    }
}
'''

class Contestant(ContestantTemplate):
    def action(self, game_log:dict) -> Action:
        opponents_last_move = None
        if game_log['opponents']['moves'][0]:
            opponents_last_move = game_log['opponents']['moves'][0][-1]

        if opponents_last_move == Action.ROCK:
            return Action.PAPER
        elif opponents_last_move == Action.PAPER:
            return Action.SCISSOR
        else: # initial move and if self.previous_actions['opponent'] == Action.SCISSOR:
            return Action.ROCK