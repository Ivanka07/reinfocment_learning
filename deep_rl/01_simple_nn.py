import gym
import tensorflow as tf 
import numpy as np

print('Starting up Gym with version %s' % gym.__version__)

def train(inputs, hidden, outputs, steps, episodes):
	initializer = tf.contrib.layers.variance_scaling_initializer()
	input_pl = tf.placeholder(tf.float32, shape=[None, inputs])

	hl1 = tf.layers.dense(input_pl, hidden, activation =tf.nn.relu, kernel_initializer=initializer, name='hl1')
	hl2 = tf.layers.dense(hl1, hidden, activation =tf.nn.relu, kernel_initializer=initializer, name='hl2')
	output = tf.layers.dense(hl2, outputs, activation =tf.nn.sigmoid, kernel_initializer=initializer, name='output')

	probabilities = tf.concat(axis=1, values=[output, 1-output])
	action = tf.multinomial(probabilities, num_samples=1)

	env = gym.make('CartPole-v1')
	avg_steps = []
	
	with tf.Session() as sess:
		sess.run(tf.global_variables_initializer())
		for episode in range(episodes):	
			observation = env.reset()
			for step in range(steps):
				action_value = action.eval(feed_dict={input_pl:observation.reshape(1, inputs)})
				print('Action value = %s' % action_value)
				observation, reward, done, infpo = env.step(action_value[0][0])
				if done:
					avg_steps.append(step)
					print('Done after {} step'.format(step))

		print('After {} Episodes, avarage steps pre game was {}'.format(episodes, np.mean(abg_steps)))



train(4,4,1, 500, 500)
