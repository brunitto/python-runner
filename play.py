from sys import exit

# Stage class
class Stage(object):

    def __init__(self):
        self.engine = Engine()

    def play(self):
        print "Stage"

    def look(self):
        print "Look"

    def talk(self):
        print "Talk"

    def joke(self):
        print "Joke"

    def fight(self):
        print "Fight"


# Stage1 class
class Stage1(Stage):

    def play(self):
        print "Stage 1"


# Stage2 class
class Stage2(Stage):

    def play(self):
        print "Stage 2"


# Stage3 class
class Stage3(Stage):

    def play(self):
        print "Stage 3"


# Stage4 class
class Stage4(Stage):

    def play(self):
        print "Stage 4"

# GameOver class
class GameOver(Stage):

    def play(self):
        print "GAME OVER!"


# Engine class
class Engine(object):

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
        return self.current_state

    def play(self):
        while self.current_state != self.states["final"]:
            stage = globals()[self.current_state]()
            stage.play()
            action = raw_input("> ")
            if action == "look":
                stage.look()
                for transition in self.states["transitions"]:
                    if transition["input"] == "look" and transition["current"] == self.current_state:
                        self.current_state = transition["next"]
                        continue
            elif action == "talk":
                stage.talk()
                for transition in self.states["transitions"]:
                    if transition["input"] == "talk" and transition["current"] == self.current_state:
                        self.current_state = transition["next"]
                        continue
            elif action == "joke":
                stage.joke()
                for transition in self.states["transitions"]:
                    if transition["input"] == "joke" and transition["current"] == self.current_state:
                        self.current_state = transition["next"]
                        continue
            elif action == "fight":
                stage.fight()
                for transition in self.states["transitions"]:
                    if transition["input"] == "fight" and transition["current"] == self.current_state:
                        self.current_state = transition["next"]
                        continue
            elif action == "quit":
                break
                exit(0)
            elif action == "help":
                print "Help: valid commands are look, talk, joke, fight, help and quit"
            else:
                print "Invalid action, try something else."


# Start the engine and play
engine = Engine()
engine.play()

