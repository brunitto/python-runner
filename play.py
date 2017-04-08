"""play.py"""

class Stage(object):
    """Stage class"""

    def __init__(self):
        """Initialize a stage"""
        self.engine = Engine()

    def play(self):
        """Describes the stage"""
        print "Stage"

    def look(self):
        """Describe the look transition"""
        print "Look"

    def talk(self):
        """Describe the talk transition"""
        print "Talk"

    def joke(self):
        """Describe the joke transition"""
        print "Joke"

    def fight(self):
        """Describe the fight transition"""
        print "Fight"


class Stage1(Stage):
    """Stage1 class"""

    def play(self):
        """Play the stage"""
        print "Stage 1"

class Stage2(Stage):
    """Stage2 class"""

    def play(self):
        """Play the stage"""
        print "Stage 2"


class Stage3(Stage):
    """Stage3 class"""

    def play(self):
        """Play the stage"""
        print "Stage 3"


class Stage4(Stage):
    """Stage4 class"""

    def play(self):
        """Play the stage"""
        print "Stage 4"


class GameOver(Stage):
    """GameOver class"""

    def play(self):
        """Play the stage"""
        print "GAME OVER!"


class Player(object):
    """Player class"""
    def __init__(self, name, health, money):
        """Initialize a player"""
        self.name = name
        self.health = health
        self.money = money


class Replicant(object):
    """Replicant class"""
    def __init__(self, name, health, reward):
        """Initialize a replicant"""
        self.name = name
        self.health = health
        self.reward = reward


class Fight(object):
    """Fight class"""
    def __init__(self, player, replicant):
        """Initialize a fight"""
        self.player = player
        self.replicant = replicant


class Engine(object):
    """Engine class"""

    stages = {
        "initial": "Stage1",
        "final": "GameOver",
        "transitions": [
            {
                "input": "look",
                "current": "Stage1",
                "next": "Stage2"
            },
            {
                "input": "talk",
                "current": "Stage2",
                "next": "Stage3"
            },
            {
                "input": "joke",
                "current": "Stage3",
                "next": "Stage4"
            },
            {
                "input": "fight",
                "current": "Stage4",
                "next": "GameOver"
            }
        ]
    }

    current_stage = stages["initial"]

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

            stage = globals()[self.current_stage]()
            stage.play()

            action = raw_input("> ")
            if action == "look":
                stage.look()
                self.current_stage = self.next_stage("look")
            elif action == "talk":
                stage.talk()
                self.current_stage = self.next_stage("talk")
            elif action == "joke":
                stage.joke()
                self.current_stage = self.next_stage("joke")
            elif action == "fight":
                stage.fight()
                self.current_stage = self.next_stage("fight")
            elif action == "quit":
                break
            elif action == "help":
                print "Help: valid commands are look, talk, joke, fight, help and quit"
            else:
                print "Invalid action, try something else."

        exit(0)


ENGINE = Engine()
ENGINE.play()
