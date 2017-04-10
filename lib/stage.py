"""stage.py"""

from lib.console import Console


class Stage(object):
    """Stage class"""

    def __init__(self):
        self.console = Console()

    def desc(self):
        """Describes the stage"""
        self.console.simulate_typing("This is a generic stage.")

    def look(self):
        """Look action"""
        print "Look"

    def talk(self):
        """Talk action"""
        print "Talk"

    def joke(self):
        """Joke action"""
        print "Joke"

    def fight(self):
        """Fight action"""
        print "Fight"

    def attack(self):
        """Attack action"""
        print "Attack"

    def roll(self):
        """Roll action"""
        print "Roll"
