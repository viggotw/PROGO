from games.contestant_general import ContestantGeneral
from enum import Enum

class Action(Enum):
    ROCK = 'rock'
    PAPER = 'paper'
    SCISSOR = 'scissor'

class ContestantTemplate(ContestantGeneral):
    def reset(self):
        pass  # TODO: Extend this