import gym
import sys

print('Starting up with gym version = %s' % gym.__version__)

env = gym.make('CartPole-v0')
print('Action space description ', env.action_space)
print('Observation  space description ', env.observation_space)

obs = env.reset()
for t in range(1000):
	if len(sys.argv)>1 and sys.argv[1] == 'render':
		env.render()
	cart_pos, cart_vel, pole_ang, ang_vel = obs
	
	if pole_ang > 0:
		action = 1
	else:
		action = 0
	obs, reward, done, info = env.step(action)
	print('Observation ', obs)
	print('Reward ', reward)

