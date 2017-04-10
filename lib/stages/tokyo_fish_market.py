"""tokyo_fish_market.py"""

from lib.stage import Stage


class TokyoFishMarket(Stage):
    """Tokyo Fish Market stage"""
    def desc(self):
        """Desc action"""
        self.console.simulate_typing("Tokyo Fish Market")
