from otree.api import *


doc = """
A simple Tullock
"""


class C(BaseConstants):
    NAME_IN_URL = 'contest'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# PAGES
class Intro(Page):
    pass


class SetupRound(WaitPage):
    pass


class Decision(Page):
    pass

class WaitForDecision(WaitPage):
    pass


class Results(Page):
    pass


class EndBlock(Page):
    pass

page_sequence = [
    Intro,
    SetupRound,
    Decision,
    WaitForDecision,
    Results,
    EndBlock,
    ]
