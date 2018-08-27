import random
from enum import Enum
from SimpleGridAction import *

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
        self.posX  = start_cell[0]
        self.posY = start_cell[1]
        self.orientation = SimpleOrientation.UP
        self.length = length
        self.actions = None
        self.rewards = None

    def get_observations(self):
        '''
        Observatiom is Agent position in the grid and orientaion
        '''
        return [self.posX, self.posY, self.orientation]


    def set_actions(self, actions):
        '''
        :param actions: dictionary: (posX, posY): list of possible actions
        '''
        self.actions = actions

    def set_states(self):
        assert self.length != None
        for x in range(0, self.length):
            for y in range(0, self.length):      
                self.states.append((x,y)) 


    def set_rewards(self, rewards):
        '''
        :param rewards: dictionary:(posX, posY)
        '''
        self.rewards = rewards
    
    def reward(self, posX, posY):
        assert self.rewards != None, 'Define the rewards first'
        r = self.rewards[(posX, posY)]
        if r!=None:
            return r
        else:
            return 0


    def is_done(self):
    	return (self.posX == self.finish_cell[0] and self.posY == self.finish_cell[1]) 


    def perform_action(self, action):
        if self.is_done():
            raise Exception('Nothing to do. Game is over!')
        if type(action) == MoveAndTurnAction:
            if action == self.actions[0] or action == self.actions[1]:
                self.get_orientation(action)
            else:
                self.get_position(action)
        elif type(action) == OnlyMoveAction:
            only_move_action(action)    
        return self.reward(self.posX, self.posY)

    
    def get_states(self):
        assert self.actions != None, 'Define the actions first'
        assert self.rewards != None, 'Define the rewards first'
        return set(self.actions.keys() + self.rewards.keys())    
    
    def only_move_action(self, action):
        assert self.actions != None, 'Define the actions first'
        if action == OnlyMoveAction.MOVE_LEFT:
            if self.posX > 0:
                self.posX -= 1
        elif action == OnlyMoveAction.MOVE_RIGHT:
            if self.posX < (self.length -1):
                self.posX += 1
        elif action == OnlyMoveAction.MOVE_UP:
            if self.posY > 0:
                self.posX -= 1
        elif action == OnlyMoveAction.MOVE_DOWN:
            if self.posY < (self.length-1):
                self.posX += 1
    
    def get_orientation(self, action):
        if self.orientation == SimpleOrientation.UP:
            if action == SimpleGridAction.TURN_LEFT:
                self.orientation = SimpleOrientation.LEFT
            elif action == SimpleGridAction.TURN_RIGHT:
                self.orientation = SimpleOrientation.RIGHT

        elif self.orientation == SimpleOrientation.DOWN:
            if action == SimpleGridAction.TURN_LEFT:
                self.orientation = SimpleOrientation.RIGHT
            elif action == SimpleGridAction.TURN_RIGHT:
                self.orientation = SimpleOrientation.LEFT

        elif self.orientation == SimpleOrientation.RIGHT:
            if action == SimpleGridAction.TURN_LEFT:
                self.orientation = SimpleOrientation.UP
            elif action == SimpleGridAction.TURN_RIGHT:
                self.orientation = SimpleOrientation.DOWN

        elif self.orientation == SimpleOrientation.LEFT:
            if action == SimpleGridAction.TURN_LEFT:
                self.orientation = SimpleOrientation.DOWN
            elif action == SimpleGridAction.TURN_RIGHT:
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
