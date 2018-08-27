from SimpleGridEnvironment import  SimpleGridEnvironment
#from SimpleAgent import SimpleAgent
from SimpleGridAction import *

if __name__ == '__main__':
	reward = 0
	act = OnlyMoveAction.MOVE_LEFT
	print(type(act) == OnlyMoveAction)
	#env = SimpleGridEnvironment([0,2],[2,0], 3)
	#agent  = SimpleAgent()
	#agent.step(env)
