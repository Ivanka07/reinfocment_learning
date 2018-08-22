import gym
import tensorflow as tf 
import numpy as np

print('Starting up Gym with version ', gym.__version__)

num_inputs = 4
num_hidden = 4
num_outputs = 1 
#initializer =
env = gym.make('CartPole-v0')
init_observation = env.reset()

for _ in range(1000):
#	env.render()
	action = env.action_space.sample()
	obs, r, done, info = env.step(action)
	print('Observation \n', obs)
	print('Reward \n', r)
	print('Done? \n', done)
	print('Info \n', info)

