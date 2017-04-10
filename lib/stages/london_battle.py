"""london_battle.py"""

from lib.stage import Stage


class LondonBattle(Stage):
    """London Battle stage"""

    def desc(self):
        """Describe action"""
        self.console.simulate_typing("London Battle")