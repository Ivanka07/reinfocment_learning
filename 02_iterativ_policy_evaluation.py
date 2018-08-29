import numpy as np
import sys
import math
sys.path.insert(0, './simplistic_world')
from SimpleGridEnvironment import *
from SimpleGridAction import OnlyMoveAction

#variation defined in Satton/Barto Book
def iterativ_policy_eval_satton_barto(grid, thr=0.001, prob=0.25,  iter=1000):
    '''
    V(s) of start/end states are 0.0
    For performing invalid states we take V(s) and Reward defined in rewards
    '''
    V = {}
    states = grid.get_states()
    for s in states:
        V[s] = 0.0
    for k in range(0, iter):
        print('-------------- Iteration  = %s ---------------' % k)
        print('Old Value function for this iteration = %s' %V )
        delta = 0
        V_old = V.copy()
        for s in states:
            if s  == grid.start_cell or s == grid.finish_cell:
                continue
            possible_actions = grid.actions[s]
            v_new = 0
            for a in possible_actions:
                s_prime = grid.next_state(s,a)
                v_new += V_old[s_prime] - 1.0
            for a in range(4 - len(possible_actions)):
                v_new +=(V_old[s]-1.0)
            
            V[s] = v_new*prob
            delta = max(delta, abs(V[s]- V_old[s]))
        if delta < thr:
            print('Delta = ', delta)
            break
    
    print('--Final value function --')
    for s in states:
        print('On state = %s, value func is= %s' % (s, V[s]))


def iterativ_policy_eval(grid, thr=0.001, prob=0.25, gamma=1.0, iter=1000):
    '''
    V(s) of start/end states are 0.0
    For performing invalid states we take V(s) and Reward defined in rewards
    '''
    V = {}
    states = grid.get_states()
    for s in states:
        V[s] = 0.0
    for k in range(0, iter):
        print('-------------- Iteration  = %s ---------------' % k)
        print('Old Value function for this iteration = %s' %V )
        delta = 0
        #V_old = V.copy()
        for s in states:
            v_old = V[s]
            if s  == grid.start_cell or s == grid.finish_cell:
                continue
            v_new = 0
            possible_actions = grid.actions[s]
            for a in possible_actions:
                print('Current action = ', a)
                grid.set_state(s)
                reward = grid.perform_action(a) 
                print('I will get reward = ', reward)
                print('Current state=', (grid.posX, grid.posY))
                #s_prime = grid.next_state(s,a)
                current_state =  (grid.posX, grid.posY)
                v_new += prob * (reward + gamma*V[current_state])
            
            V[s] = v_new
            delta = max(delta, abs(V[s]- v_old))
        if delta < thr:
            print('Delta = ', delta)
            break
    
    print('--Final value function --')
    for s in states:
        print('On state = %s, value func is= %s' % (s, V[s]))

if __name__ == '__main__':
    print('Creating a grid environment first')
    env = SimpleGridEnvironment([0,0], [3,3], 4)
    actions = {(0,0): [OnlyMoveAction.MOVE_DOWN, OnlyMoveAction.MOVE_RIGHT],
               (0,1): [OnlyMoveAction.MOVE_DOWN, OnlyMoveAction.MOVE_RIGHT, OnlyMoveAction.MOVE_UP],
               (0,2): [OnlyMoveAction.MOVE_DOWN, OnlyMoveAction.MOVE_RIGHT, OnlyMoveAction.MOVE_UP],
               (0,3): [OnlyMoveAction.MOVE_RIGHT, OnlyMoveAction.MOVE_UP],
               (1,0): [OnlyMoveAction.MOVE_DOWN, OnlyMoveAction.MOVE_RIGHT, OnlyMoveAction.MOVE_LEFT],
               (1,1): [OnlyMoveAction.MOVE_DOWN, OnlyMoveAction.MOVE_RIGHT, OnlyMoveAction.MOVE_UP, OnlyMoveAction.MOVE_LEFT], 
               (1,2): [OnlyMoveAction.MOVE_DOWN, OnlyMoveAction.MOVE_RIGHT, OnlyMoveAction.MOVE_UP, OnlyMoveAction.MOVE_LEFT], 
               (1,3): [OnlyMoveAction.MOVE_LEFT, OnlyMoveAction.MOVE_RIGHT, OnlyMoveAction.MOVE_UP],
               (2,0): [OnlyMoveAction.MOVE_DOWN, OnlyMoveAction.MOVE_RIGHT, OnlyMoveAction.MOVE_LEFT],
               (2,1): [OnlyMoveAction.MOVE_DOWN, OnlyMoveAction.MOVE_RIGHT, OnlyMoveAction.MOVE_UP, OnlyMoveAction.MOVE_LEFT], 
               (2,2): [OnlyMoveAction.MOVE_DOWN, OnlyMoveAction.MOVE_RIGHT, OnlyMoveAction.MOVE_UP, OnlyMoveAction.MOVE_LEFT], 
               (2,3): [OnlyMoveAction.MOVE_LEFT, OnlyMoveAction.MOVE_RIGHT, OnlyMoveAction.MOVE_UP],
               (3,0): [OnlyMoveAction.MOVE_DOWN, OnlyMoveAction.MOVE_LEFT],
               (3,1): [OnlyMoveAction.MOVE_DOWN, OnlyMoveAction.MOVE_LEFT, OnlyMoveAction.MOVE_UP], 
               (3,2): [OnlyMoveAction.MOVE_DOWN, OnlyMoveAction.MOVE_LEFT, OnlyMoveAction.MOVE_UP], 
               (3,3): [OnlyMoveAction.MOVE_LEFT, OnlyMoveAction.MOVE_UP]
               }
    
    
    rewards = {(0,0):0.0, 
               (0,1):-1.0, 
               (0,2):-1.0, 
               (0,3):-1.0,
               (1,0):-1.0,
               (1,1):-1.0,
               (1,2):-1.0,
               (1,3):-1.0, 
               (2,0):-1.0, 
               (2,1):-1.0, 
               (2,2):-1.0, 
               (2,3):-1.0,
               (3,0):-1.0,
               (3,1):-1.0,
               (3,2):-1.0,
               (3,3): 0.0
               }
    
    env.set_rewards(rewards)
    env.set_actions(actions)
    
    env2 = SimpleGridEnvironment([2,0], [0,3], 4)
    rewards = {(0,0): 0.0, 
               (0,1): 0.0, 
               (0,2): 0.0, 
               (0,3): 1.0,
               (1,0): 0.0,
               (1,1): 0.0,
               (1,2): 0.0,
               (1,3):-1.0, 
               (2,0): 0.0, 
               (2,1): 0.0, 
               (2,2): 0.0, 
               (2,3): 0.0,
               (3,0): 0.0,
               (3,1): 0.0,
               (3,2): 0.0,
               (3,3): 0.0
               }
    
    env2.set_rewards(rewards2)
    env2.set_actions(actions)
    print(env.get_states())
    #iterativ_policy_eval(actions, rewards)
    iterativ_policy_eval(env)
