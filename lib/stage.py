"""stage.py"""

from lib.console import Console


class Stage(object):
    """Stage class"""

    def __init__(self):
        self.console = Console()

    def desc(self):
        """Describes the stage"""

        action = """
This is a generic stage.
"""
        self.console.simulate_typing(action)

    def look(self):
        """Look action"""

        action = """
You look around, nothing happens
"""
        self.console.simulate_typing(action)

    def talk(self):
        """Talk action"""

        action = """
You talk with no one, nothing happens
"""
        self.console.simulate_typing(action)

    def joke(self):
        """Joke action"""

        action = """
You drop an epic joke, nothing happens
"""
        self.console.simulate_typing(action)

    def fight(self):
        """Fight action"""

        action = """
You start a fight, alone, nothing happens
"""

        self.console.simulate_typing(action)

    def attack(self):
        """Attack action"""

        action = """
You attack, the air, nothing happens
"""
        self.console.simulate_typing(action)

    def roll(self):
        """Roll action"""
        
        action = """
You roll over, alone, nothing happens
"""
        self.console.simulate_typing(action)
