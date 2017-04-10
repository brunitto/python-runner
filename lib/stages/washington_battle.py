"""washington_battle.py"""

from lib.stage import Stage


class WashingtonBattle(Stage):
    """Washington Battle stage"""

    def desc(self):
        """Describe action"""
        self.console.simulate_typing("Washington Battle")
