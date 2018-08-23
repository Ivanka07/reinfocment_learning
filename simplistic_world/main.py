from SimpleGridEnvironment import  SimpleGridEnvironment
from SimpleAgent import SimpleAgent

if __name__ == '__main__':
	reward = 0
	env = SimpleGridEnvironment([0,2],[2,0], 3)
	agent  = SimpleAgent()
	agent.step(env)