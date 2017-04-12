"""tokyo_fish_market.py"""

from lib.stage import Stage


class TokyoFishMarket(Stage):
    """Tokyo Fish Market stage"""
    def desc(self):
        """Desc action"""

        action = """
It's about 8AM and you are in a famous fish market in Tokyo. Some contacts
told you about a really strange man fooling around, getting angry everytime
someone drops a good joke. Everything smells like fish and a lot of different
noises. All of sudden, at your left, looks like someone is getting closer...
"""
        self.console.simulate_typing(action)

    def look(self):
        """Look action"""

        action = """
You look at your left...
"""
        self.console.simulate_typing(action)

    def talk(self):
        """Talk action"""

        action = """
There are too many people, no one listens to what you are talking...
"""
        self.console.simulate_typing(action)

    def joke(self):
        """Joke action"""

        action = """
The people can't hear your joke, if you had a megaphone...
"""
        self.console.simulate_typing(action)

    def fight(self):
        """Fight action"""

        action = """
You try to start a random fight, but everyone is looking for a good sushi...
"""
        self.console.simulate_typing(action)
