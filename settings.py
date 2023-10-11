from enum import Enum

# Setting up some enums for directions
class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

# some game settings
WINDOW_WIDTH = 60
WINDOW_HEIGHT = 20
SNAKE_LENGTH = 5
TIMEOUT = 100
