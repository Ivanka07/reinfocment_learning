import numpy as np
import tensorflow as tf
import gym
import sys
sys.path.insert(0, '../utilities')
import files

def cumulative_discounted_rewards(rewards, discount_rate):
    '''
    :param rewards: rewards for an episode
    :param discount_rate: discount rare 
    :returns discounted_rewards: a list with cumulated discounted rewards
    d_r = r1 + r2*discount_rate^1 + ... + rN*discount_rate*N
    '''
    discounted_rewards = np.zeros(len(rewards))
    cumulative_rewards = 0
    for step in reversed(range(len(rewards))):
        cumulative_rewards = rewards[step] + cumulative_rewards * discount_rate
        discounted_rewards[step] = cumulative_rewards
    return discounted_rewards


def discount_and_normilize_rewards(all_rewards, discount_rate):
    '''
    :param all_rewards: list of lists with rewards for all episods
    :param discount rate: discount factor
    :return list: normilized rewards by mean and standard deviation
    '''
    normilized_rewards = []
    all_disc_rewards = []
    for rewards in all_rewards:
        all_disc_rewards.append(cumulative_discounted_rewards(rewards, discount_rate))
    flat_rewards = np.concatenate(all_disc_rewards)
    rewards_mean = flat_rewards.mean()
    rewards_std = flat_rewards.std()
    normilized_rewards =  [(discounted_rewards - rewards_mean)/ rewards_std for discounted_rewards in all_disc_rewards]
    return normilized_rewards



def train_model(env, games, steps, epochs, input_num=4, hidden_num=4, output_num=1, learning_rate=0.01):

    X, gradients, action, grad_placeholders, training_optimizer = build_network(input_num, output_num, hidden_num)

    saver = tf.train.Saver()

    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        for epoch in range(epochs):
            print('Performing iteration: %d' % epoch)
            _rewards = []
            _gradients = []
            #we play N times  10 rounds of the game  and collect the rewards
            for game in range(games):
                current_rewards = []
                current_gradients = []
                observations = env.reset()

                for step in range(steps):
                    observations = observations.reshape(1, input_num)
                    action_value, gradients_value = sess.run([action, gradients], feed_dict = {X: observations})
                    observations, reward, done, info  = env.step(action_value[0][0])
                    current_rewards.append(reward)
                    current_gradients.append(gradients_value)

                    if done:
                        break
                _rewards.append(current_rewards)
                _gradients.append(current_gradients)
                #multiplying adjusted scores with discounts against the gradients
            _rewards = discount_and_normilize_rewards(_rewards, discout_rate)
            feed_dict = {}

            for var_index, gradient_placeholder in enumerate(grad_placeholders):
                for game_index, rewards in enumerate(_rewards):
                    print('Game index =', game_index)                
                mean_gradients =  np.mean([reward * _gradients[game_index][step][var_index]  for game_index, rewards in enumerate(_rewards) for step, reward in enumerate(rewards)], axis=0)
                feed_dict[gradient_placeholder] = mean_gradients
            sess.run(training_optimizer, feed_dict=feed_dict)
        #create_dir('models')
        meta_graph_def = tf.train.export_meta_graph(filename='./models/' + str(epochs) + '-step-model.meta')
        saver.save(sess, './models/' + str(epochs) + '-step-model')


def build_network(input_num, output_num, hidden_num, learning_rate=0.01):
    discout_rate = 0.95 
    initalizer = tf.contrib.layers.variance_scaling_initializer()
    X = tf.placeholder(tf.float32, shape=[None, 4])
    h1 = tf.layers.dense(X, 4, activation=tf.nn.elu, kernel_initializer=initalizer)
    logits = tf.layers.dense(h1, 1)
    output_probs = tf.nn.sigmoid(logits)
    probs = tf.concat(axis=1, values=[output_probs, 1-output_probs])
    action = tf.multinomial(probs, num_samples=1) 
    y = 1.0 - tf.to_float(action)
    cross_entropy = tf.nn.sigmoid_cross_entropy_with_logits(labels=y, logits=logits)
    adam_optimizer = tf.train.AdamOptimizer(learning_rate)
    gradiants_variables = adam_optimizer.compute_gradients(cross_entropy)

    gradients = []
    grad_placeholders = []
    grad_vars_feed = []
    for g, v in gradiants_variables:
        gradients.append(g)
        grad_plholder = tf.placeholder(tf.float32, shape=g.get_shape())
        grad_placeholders.append(grad_plholder)
        grad_vars_feed.append((grad_plholder, v))

    training_optimizer = adam_optimizer.apply_gradients(grad_vars_feed)
    
    return X, gradients, action, grad_placeholders, training_optimizer




def run_model(env, path_to_model):
    
    X, gradients, action, _, _ = build_network(4, 1, 4)
    
    with tf.Session() as sess:
        new_saver = tf.train.import_meta_graph(path_to_model + '.meta') 
        new_saver.restore(sess, path_to_model)
        observations = env.reset()
        for x in range(500):
            env.render()
            action_val, gradients_val = sess.run([action, gradients], feed_dict={X: observations.reshape(1, 4)})
            observations, reward, done, info = env.step(action_val[0][0])
    
if __name__ == '__main__':
    env = gym.make('CartPole-v1')
    games = 10
    max_game_steps = 1000
    iterations = 500
    #train(env, 10, 1000, 500)
    run_model(env, './models/'+ str(iterations) + '-step-model')
