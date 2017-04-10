"""tokyo_battle.py"""

from lib.stage import Stage


class TokyoBattle(Stage):
    """Tokyo Battle stage"""

    def desc(self):
        """Describe action"""
        self.console.simulate_typing("Tokyo Battle")
