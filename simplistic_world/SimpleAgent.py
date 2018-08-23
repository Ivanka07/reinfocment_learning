import random

class SimpleAgent:
	
    def __init__(self):
    	self.total_reward = 0.0

    def step(self, env):
        print('Current observations = %s' % env.get_observations())    	
        print('Action space = %s' % env.get_actions())
        possible_actions = env.get_actions()
        random_action = random.choice(possible_actions)
        print('Chose random action=%s to perfom' % random_action)
        env.perform_action(random_action) 
        print('Updated observations = %s' % env.get_observations())