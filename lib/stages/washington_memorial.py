"""washington_memorial.py"""

from lib.stage import Stage


class WashingtonMemorial(Stage):
    """Washington Memorial stage"""

    def desc(self):
        """Describe action"""

        action = """
After nailing down another replicant, you check your Twitter timeline and 
there are a lot of people talking a big mess in Washington, with a lot of
hipsters-like people protesting against good jokes. You get an Uber and
arrive to a big memorial. You look to a giant guy sitting on a stone chair
and it's does not looks like a replicant. Everyone is in bad mood and no
one is listening to anyone...
"""
        self.console.simulate_typing(action)

    def look(self):
        """Look action"""

        action = """
You look around, it's a riot, some violence might work...
"""
        self.console.simulate_typing(action)

    def talk(self):
        """Talk action"""

        action = """
No one is listening to you, it's a riot...
"""
        self.console.simulate_typing(action)

    def joke(self):
        """Joke action"""

        action = """
You start telling a joke, in a riot against jokes, everyone beats the shit
out of you...
"""
        self.console.simulate_typing(action)

    def fight(self):
        """Fight action"""

        action = """
You punches some random guy in the face. Everyone start fighting...
"""
        self.console.simulate_typing(action)
