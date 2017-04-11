"""death.py"""

from lib.stage import Stage


class Death(Stage):
    """Death stage"""
    def desc(self):
        """Describe action"""
        self.console.simulate_typing("YOU DIED! YOU SUCK!")
        exit(1)
