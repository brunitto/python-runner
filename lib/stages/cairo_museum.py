"""cairo_museum.py"""

from lib.stage import Stage


class CairoMuseum(Stage):
    """Cairo Museum stage"""

    def desc(self):
        """Describe action"""
        self.console.simulate_typing("Cairo Museum")
