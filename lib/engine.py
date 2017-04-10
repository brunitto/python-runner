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
        while self.current_stage != self.stages["final"]:

            # Get the stage class symbol using the stage name as string
            stage = globals()[self.current_stage]()
            stage.desc()

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
