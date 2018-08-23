import random

class SimpleAgent:
	
    def __init__(self):
    	self.total_reward = 0.0

    def step(self, env):
    	print('Current observations = %s' % env.get_observations())    	
    	print('Action space = %s' % env.get_actions())
    	
        