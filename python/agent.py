import numpy as np
from enum import Enum

'''Character Moves'''
class Moves(Enum):
	NO_ACTION = 0
	ROLL_LEFT = 1
	ROLL_RIGHT = 2
	JUMP = 3
	GROW = 4
	MOVE_LEFT = 5
	MOVE_RIGHT = 6
	MORPH_UP = 7
	MORPH_DOWN = 8

'''Agent Class'''
class Agent:
	def __init__(self, name, env):
		self.name = name
		self.env = env
		self.currentAction = 0
	
	#TODO: messages between agents? 

'''Circle Agent Class'''
class CircleAgent(Agent):
	def __init__(self, name, env):
		super().__init__(name, env)
		self.possibleMoves = [Moves.ROLL_LEFT.value, Moves.ROLL_RIGHT.value, Moves.JUMP.value]
		self.lenMoves = len(self.possibleMoves)
	
	def randomAction(self):
		self.currentAction = np.random.randint(0, self.lenMoves)
		
	def executeAction(self):
		self.randomAction()

'''Rectangle Agent Class'''
class RectangleAgent(Agent):
	def __init__(self, name, env):
		super().__init__(name, env)
		self.possibleMoves = [Moves.MOVE_LEFT.value, Moves.MOVE_RIGHT.value, Moves.MORPH_UP.value, Moves.MORPH_DOWN.value]
		self.lenMoves = len(self.possibleMoves)
	
	def randomAction(self):
		self.currentAction = np.random.randint(0, self.lenMoves)

	def executeAction(self):
		self.randomAction()
