"""RaiseBot"""
from typing import Sequence

from bots.BotInterface import BotInterface
from environment.Constants import Action
from environment.Observation import Observation


# your bot class, rename to match the file name
class RaiseBot(BotInterface):

    # change the name of your bot here
    def __init__(self, name="RaiseBot"):
        '''init function'''
        super().__init__(name=name)

    def act(self, action_space: Sequence[Action], observation: Observation) -> Action:
        return Action.RAISE
