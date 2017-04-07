from sys import exit

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


class Stage1(Stage):

    def play(self):
        print "Stage 1"


class Stage2(Stage):

    def play(self):
        print "Stage 2"


class Stage3(Stage):

    def play(self):
        print "Stage 3"


class Stage4(Stage):

    def play(self):
        print "Stage 4"


class GameOver(Stage):

    def play(self):
        print "GAME OVER!"


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
                # DRY
                transition = [t for t in self.states["transitions"] \
                    if t["input"] == action and t["current"] == self.current_state][0]
                self.current_state = transition["next"]
                continue
            elif action == "talk":
                stage.talk()
                # DRY
                transition = [t for t in self.states["transitions"] \
                    if t["input"] == action and t["current"] == self.current_state]
                self.current_state = transition["next"]
                continue
            elif action == "joke":
                stage.joke()
                # DRY
                transition = [t for t in self.states["transitions"] \
                    if t["input"] == action and t["current"] == self.current_state]
                self.current_state = transition["next"]
                continue
            elif action == "fight":
                stage.fight()
                # DRY
                transition = [t for t in self.states["transitions"] \
                    if t["input"] == action and t["current"] == self.current_state]
                self.current_state = transition["next"]
                continue
            elif action == "quit":
                break
            elif action == "help":
                print "Help: valid commands are look, talk, joke, fight, help and quit"
            else:
                print "Invalid action, try something else."


Engine().play()
