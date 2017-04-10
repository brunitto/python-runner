"""cairo_battle.py"""

from lib.stage import Stage


class CairoBattle(Stage):
    """Cairo Battle stage"""

    def desc(self):
        """Describe action"""
        self.console.simulate_typing("Cairo Battle")
