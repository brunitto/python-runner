"""london_abbey.py"""

from lib.stage import Stage


class LondonAbbey(Stage):
    """London Abbey stage"""

    def desc(self):
        """Describe action"""

        action = """
After getting the second replicant. You search in Google and find that are
some people talking about a strange royal guard that arrests people for
telling good jokes. You take the next ship to London and get in a fancy and
old Abbey. There is no one around and a confortable silence...
"""
        self.console.simulate_typing(action)

    def look(self):
        """Look action"""

        action = """
You look around, there are some guards and everything looks royal...
"""
        self.console.simulate_typing(action)

    def talk(self):
        """Talk action"""

        action = """
You talk to a royal guard, but they are famous for give a shit about it...
"""
        self.console.simulate_typing(action)

    def joke(self):
        """Joke action"""

        action = """
You drop an epic joke, almost every guard laughs...
"""
        self.console.simulate_typing(action)

    def fight(self):
        """Fight action"""

        action = """
It's not a good idea to fight inside an abbey, so barbaric...
"""
        self.console.simulate_typing(action)
