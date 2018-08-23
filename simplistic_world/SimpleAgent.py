import random

class SimpleAgent:
	'''
	Agent has only total reward
	'''
    def __init__(self):
    	self.total_reward = 0.0

    def step(self, env):
    	print('Current observation = %s' % env.get_observation())    	
    	print('Current actions possible = %s' % env.get_actions())
    	action = random.choise(env.get_actions())
    	print('Action = %s is chosen' % action)
    	reward = env.action(action)
    	self.total_reward += reward  
