"""washington_battle.py"""

from lib.stage import Stage


class WashingtonBattle(Stage):
    """Washington Battle stage"""

    def desc(self):
        """Describe action"""

        action = """
In the heat of the riot, a really big and bearded guy, riding a noisy
motorcyle rushes over you, swinging a chain in fire... time to fight!
"""
        self.console.simulate_typing(action)

    def attack(self):
        """Attack action"""

        action = """
You get your shotgun and shoot, but the replicant reflects your bullets using
the chain and kicks you in the ass to the middle of the riot, disarmed and
helpless... 
"""
        self.console.simulate_typing(action)

    def roll(self):
        """Roll action"""

        action = """
You roll forward and shoot the motorcycle gas tank. It explodes, killing the
replicant leaders and dispersing the riot... good job!
"""
        self.console.simulate_typing(action)
