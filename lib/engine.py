"""engine.py"""

from lib.stages.death import Death
from lib.stages.final import Final
from lib.stages.tokyo_fish_market import TokyoFishMarket
from lib.stages.tokyo_battle import TokyoBattle
from lib.stages.cairo_museum import CairoMuseum
from lib.stages.cairo_battle import CairoBattle
from lib.stages.london_abbey import LondonAbbey
from lib.stages.london_battle import LondonBattle
from lib.stages.washington_memorial import WashingtonMemorial
from lib.stages.washington_battle import WashingtonBattle

class Engine(object):
    """Engine class"""

    stages = {
        "initial": "TokyoFishMarket",
        "final": "Final",
        "transitions": [
            {
                "current": "TokyoFishMarket",
                "input": "look",
                "next": "TokyoBattle"
            },
            {
                "current": "TokyoBattle",
                "input": "attack",
                "next": "Death"
            },
            {
                "current": "TokyoBattle",
                "input": "roll",
                "next": "CairoMuseum"
            },
            {
                "current": "CairoMuseum",
                "input": "talk",
                "next": "CairoBattle"
            },
            {
                "current": "CairoBattle",
                "input": "roll",
                "next": "Death"
            },
            {
                "current": "CairoBattle",
                "input": "attack",
                "next": "LondonAbbey"
            },
            {
                "current": "LondonAbbey",
                "input": "joke",
                "next": "LondonBattle"
            },
            {
                "current": "LondonBattle",
                "input": "roll",
                "next": "Death"
            },
            {
                "current": "LondonBattle",
                "input": "attack",
                "next": "WashingtonMemorial"
            },
            {
                "current": "WashingtonMemorial",
                "input": "fight",
                "next": "WashingtonBattle"
            },
            {
                "current": "WashingtonMemorial",
                "input": "joke",
                "next": "Death"
            },
            {
                "current": "WashingtonBattle",
                "input": "attack",
                "next": "Death"
            },
            {
                "current": "WashingtonBattle",
                "input": "roll",
                "next": "Final"
            }
        ]
    }

    current_stage = stages["initial"]

    valid_actions = [
        "desc", "look", "talk", "joke", "fight", "attack", "roll", "help", "quit"
    ]

    def __init__(self):
        """Initialize the engine"""
        pass

    def next_stage(self, action):
        """Get the next stage from an action, passing through the FSM"""
        for transition in self.stages["transitions"]:
            if transition["input"] == action and \
                    transition["current"] == self.current_stage:
                return transition["next"]

        return self.current_stage

    def play(self):
        """Play the game"""
        print ""
        print "Welcome to Python Runner"
        print ""
        print "You're Peckard, a bounty-hunter that captures replicants for"
        print "money. The year is 2019 and some rebel replicants stole a"
        print "ship and returned to earth to make some trouble. Your mission"
        print "is to find and capture these replicants as soon as possible."
        print "There are rumours about these replicants in 4 famous capitals,"
        print "including: Tokyo, Cairo, London and Washington. The first stop"
        print "is Tokyo..."
        print ""

        raw_input("Press <ENTER> to continue...")

        played_stages = {
            "TokyoFishMarket": False,
            "CairoMuseum": False,
            "LondonAbbey": False,
            "WashingtonMemorial": False,
        }

        while self.current_stage != self.stages["final"]:

            # Get the stage class symbol using the stage name as string
            stage = globals()[self.current_stage]()

            # Avoid to describe already played stages
            if played_stages[self.current_stage]:
                pass
            else:
                stage.desc()
                played_stages[self.current_stage] = True

            action = raw_input("> ")
            if action in self.valid_actions:
                if action == "help":
                    print "Valid actions are %s" % (", ".join(self.valid_actions))
                elif action == "quit":
                    exit(0)
                else:
                    # Get the stage function symbol using the function name as string
                    stage_action = getattr(stage, action)
                    stage_action()

                    # Set the current stage to the next valid stage
                    self.current_stage = self.next_stage(action)
            else:
                print "Invalid action, try something else."

        # Play the final stage
        stage = globals()[self.stages["final"]]()
        stage.desc()

        exit(0)
