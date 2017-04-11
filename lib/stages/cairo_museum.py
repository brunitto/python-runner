"""cairo_museum.py"""

from lib.stage import Stage


class CairoMuseum(Stage):
    """Cairo Museum stage"""

    def desc(self):
        """Describe action"""

        action = """
After getting the first replicant, you call some old friends and some of them
mentions something about a hippie woman that likes no jokes. You get the next
ship to Cairo and go to a big museum. Everything smells dust and there are a
lot of camels and people around. In an isolated corner, you see a different
woman in bad mood, looking to you from time to time...
"""
        self.console.simulate_typing(action)

    def look(self):
        """Look action"""

        action = """
Everyone seens to be busy looking at the art, mainly the big statues, nothing
suspicious, except for a different woman in the corner...
"""
        self.console.simulate_typing(action)

    def talk(self):
        """Talk action"""

        action = """
You say 'hi' to the woman...
"""
        self.console.simulate_typing(action)

    def joke(self):
        """Joke action"""

        action = """
You tell a really good joke and an old mummy start laughing...
"""
        self.console.simulate_typing(action)

    def fight(self):
        """Fight action"""

        action = """
You try to start a fight, but a camel holds you and tells you to calm down...
"""
        self.console.simulate_typing(action)
