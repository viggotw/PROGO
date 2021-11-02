from games.rock_paper_scissor.contestant_custom import ContestantCustom, Action

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

class Contestant(ContestantCustom):
    def action(self, game_log:dict) -> Action.__mro__[0]:
        return Action.ROCK