"""london_battle.py"""

from lib.stage import Stage


class LondonBattle(Stage):
    """London Battle stage"""

    def desc(self):
        """Describe action"""

        action = """
A short and ugly guard did not laugh at your epic joke. Instead, he looks you
in the eyes and you known: another replicant. It rushes over getting ready to
slice you with it's royal sword... time to fight!
"""
        self.console.simulate_typing(action)

    def attack(self):
        """Attack action"""

        action = """
There is a lot of room, you just draw your shotgun, aim in the chest and
BOOM! good job!
"""
        self.console.simulate_typing(action)

    def roll(self):
        """Roll action"""

        action = """
You roll back but roll too much, and hit the head in the wall. The guard
gets you helpless and chop off your head using it's fancy sword...
"""
        self.console.simulate_typing(action)
