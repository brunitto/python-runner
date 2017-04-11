"""final.py"""

from lib.stage import Stage


class Final(Stage):
    """Final stage"""
    def desc(self):
        """Describe action"""
        self.console.simulate_typing("You got the replicants, you're awesome!")
