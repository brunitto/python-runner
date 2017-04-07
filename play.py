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


class Engine(object):
    """Engine class"""

    states = {
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

    current_state = states["initial"]

    def current(self):
        """Return the current state"""
        return self.current_state

    def play(self):
        """Play the game"""
        while self.current_state != self.states["final"]:
            stage = globals()[self.current_state]()
            stage.play()
            action = raw_input("> ")

            if action == "look":
                stage.look()
                # DRY
                for transition in self.states["transitions"]:
                    if transition["input"] == action \
                        and transition["current"] == self.current_state:
                        self.current_state = transition["next"]
            elif action == "talk":
                stage.talk()
                # DRY
                for transition in self.states["transitions"]:
                    if transition["input"] == action \
                        and transition["current"] == self.current_state:
                        self.current_state = transition["next"]
            elif action == "joke":
                stage.joke()
                # DRY
                for transition in self.states["transitions"]:
                    if transition["input"] == action \
                        and transition["current"] == self.current_state:
                        self.current_state = transition["next"]
            elif action == "fight":
                stage.fight()
                # DRY
                for transition in self.states["transitions"]:
                    if transition["input"] == action \
                        and transition["current"] == self.current_state:
                        self.current_state = transition["next"]
            elif action == "quit":
                break
            elif action == "help":
                print "Help: valid commands are look, talk, joke, fight, help and quit"
            else:
                print "Invalid action, try something else."

        exit(0)


Engine().play()
