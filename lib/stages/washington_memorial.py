"""washington_memorial.py"""

from lib.stage import Stage


class WashingtonMemorial(Stage):
    """Washington Memorial stage"""

    def desc(self):
        """Describe action"""
        self.console.simulate_typing("Washington Memorial")
