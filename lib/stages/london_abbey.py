"""london_abbey.py"""

from lib.stage import Stage


class LondonAbbey(Stage):
    """London Abbey stage"""

    def desc(self):
        """Describe action"""
        self.console.simulate_typing("London Abbey")
