# PYTHON RUNNER

Find the replicants, get the reward, do not die.

This is a really simple console game written in python, as defined in
[Learn Python the Hard Way exercise 45](https://learnpythonthehardway.org/book/ex45.html).

## Requirements

1. Python 2.7.3+

## How to play

[Download the latest release](https://github.com/brunitto/python-runner/archive/stable.zip)
at GitHub, extract and execute the `play.py` script:

    mkdir /tmp/games
    cd /tmp/games
    wget http://github.com/brunitto/python-runner/archive/stable.zip
    unzip stable.zip
    cd python-runner-stable
    python play.py

The game will describe a stage and wait for a valid command. The valid commands are:

1. `desc`: describe the stage
2. `look`: look around
3. `talk:`talk to someone
4. `joke`: drop an epic joke
5. `fight`: start a fight

Within battles:

1. `attack`: attack with the shotgun
2. `roll`: avoid the enemy attack

If you fell lost, the `help` command will help you. If you want to quit, use
the `quit` command.

## Tips

1. Replicants does not like jokes
2. Replicants are aggressive
3. If you fell lost, use the `help` command

## Finite-state Machine

This game uses the Finite-state Machine model to define the stages and the
transitions between these stages (or states). The game map is defined as a
dict within `Engine` class within `lib/engine.py` module. New stages can be
created by adding more transitions to this dict and creating new stage
classes, extending the `Stage` base class within the `lib/stage.py` module.

## Inheritance versus composition

This game use Python object-oriented features like inheritance and composition.
Each stage inherits functions from the `Stage` base class, which import
functions from the `Console` class within `lib/console.py` module.

## Issues

[Report an issue at GitHub](https://github.com/brunitto/python-runner/issues)

## Contribure

[Check the official repository at GitHub](https://github.com/brunitto/python-runner)

## References

1. [Learn Python the Hard Way](https://learnpythonthehardway.org)
2. [PEP-8](https://www.python.org/dev/peps/pep-0008)
3. [Finite-state machine](https://en.wikipedia.org/wiki/Finite-state_machine)
