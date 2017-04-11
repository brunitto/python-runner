"""cairo_battle.py"""

from lib.stage import Stage


class CairoBattle(Stage):
    """Cairo Battle stage"""

    def desc(self):
        """Describe action"""

        action = """
You get closer to the woman and she looks at your eyes and recognizes you. She
rush over you while trying to get a piece of stone nearby... time to fight!
"""
        self.console.simulate_typing(action)

    def attack(self):
        """Attack action"""

        action = """
You get your shotgun and shoots straight. You're a lucky guy, you hit the
replicant in the leg, as well as some innocent mummies, good job!
"""
        self.console.simulate_typing(action)

    def roll(self):
        """Roll action"""

        action = """
You try to roll but step on a statue and fall helpless. The replicant hits you
in the head using the stone...
"""
        self.console.simulate_typing(action)
