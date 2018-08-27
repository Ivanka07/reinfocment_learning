from enum import Enum

#class SimpleGridAction():
#    def __init__(self):
#        print('creating')

class MoveAndTurnAction(Enum):
    TURN_LEFT = 1
    TURN_RIGHT = 2
    MOVE_FORWARD = 3


class OnlyMoveAction(Enum):
	MOVE_LEFT = 1
	MOVE_RIGHT = 2
	MOVE_UP = 3
	MOVE_DOWN = 4
