import random
from enum import Enum
from SimpleGridAction import SimpleGridAction

class SimpleOrientation(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


class SimpleGridEnvironment:
    def __init__(self, start_cell, end_cell, length):
        '''
        :param start_cell: array with 2d x and y position
        :param end_cell: finish array with 2d position
        '''
        self.start_cell = start_cell
        self.finish_cell = end_cell
        self.actions = self.get_actions()
        self.posX  = start_cell[0]
        self.posY = start_cell[1]
        self.orientation = SimpleOrientation.UP
        self.length = length


    def get_observations(self):
        '''
        Observatiom is Agent position in the grid and orientaion
        '''
        return [self.posX, self.posY, self.orientation]


    def get_actions(self):
    	return [SimpleGridAction.TURN_LEFT, SimpleGridAction.TURN_RIGHT, SimpleGridAction.MOVE_FORWARD]


    def get_reward(self, action):
        '''
        Takes position and orientation of the agent, 
        the action it would perform and returns a reward
        '''
        pass   


    def is_done(self):
    	return (self.posX == self.finish_cell[0] and self.posY == self.finish_cell[1]) 


    def perform_action(self, action):
        if self.is_done():
            raise Exception('Nothing to do. Game is over!')

        if action == self.actions[0] or action == self.actions[1]:
            self.get_orientation(action)
        else:
            self.get_position(action)
        return self.get_observations()

    def get_orientation(self, action):
        if self.orientation == SimpleOrientation.UP:
            if action == self.actions[0]:
                self.orientation = SimpleOrientation.LEFT
            elif action == self.actions[1]:
                self.orientation = SimpleOrientation.RIGHT

        if self.orientation == SimpleOrientation.DOWN:
            if action == self.actions[0]:
                self.orientation = SimpleOrientation.RIGHT
            elif action == self.actions[1]:
                self.orientation = SimpleOrientation.LEFT

        if self.orientation == SimpleOrientation.RIGHT:
            if action == self.actions[0]:
                self.orientation = SimpleOrientation.UP
            elif action == self.actions[1]:
                self.orientation = SimpleOrientation.DOWN

        if self.orientation == SimpleOrientation.LEFT:
            if action == self.actions[0]:
                self.orientation = SimpleOrientation.DOWN
        elif action == self.actions[1]:
                self.orientation = SimpleOrientation.UP

        
    def get_position(self, action):
        '''
        :returns: next position of the agent
        depends on orientation and position
        '''
        if self.orientation == SimpleOrientation.UP:
            if self.posY == 0:
                return
            else:
                self.posY = self.posY - 1
        
        if self.orientation == SimpleOrientation.DOWN:
            if self.posY == self.length:
                return
            else:
                self.posY = self.posY + 1

        if self.orientation == SimpleOrientation.LEFT:
            if self.posX == 0:
                return
            else:
                self.posX = self.posY - 1
        
        if self.orientation == SimpleOrientation.RIGHT:
            if self.posX == self.length:
                return
            else:
                self.posX = self.posY + 1