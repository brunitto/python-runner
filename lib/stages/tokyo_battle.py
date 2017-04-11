"""tokyo_battle.py"""

from lib.stage import Stage


class TokyoBattle(Stage):
    """Tokyo Battle stage"""

    def desc(self):
        """Describe action"""

        action = """
You look at your left, and a tall white-haired guy says some dirty words at
you and rushes over you holding a knife... time to fight!
"""
        self.console.simulate_typing(action)

    def attack(self):
        """Attack action"""

        action = """
You try to attack the replicant, but he is too close, and you do not had
enough time to get your shotgun...
"""
        self.console.simulate_typing(action)

    def roll(self):
        """Roll action"""

        action = """
You quickly roll under some stall. The replicant misses and before he can
attack again, you draw your shotgun and shoot it in the ass, good job!
"""
        self.console.simulate_typing(action)
