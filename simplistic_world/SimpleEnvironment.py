import random

class SimpleEnvironment:
	'''
	In this very simplistic environment state is time step 
	'''
	def __init__(self):
    	self.number_of_steps = 10

    def get_observations(self):
    	return [0.0, 0.0, 0.0]

    def get_actions(self):
    	return [0, 1]

    def is_done(self):
    	return self.number_of_steps == 0

     def action(self, action):
    	if self.is_done:
    		raise Exception('Nothing to do. Done!')
    	print('Handling action=%s' % action)
    	self.number_of_steps -= 1
    	reward = random.random()
    	print('Rewarding agent with reward=%s' % reward)
    	return reward