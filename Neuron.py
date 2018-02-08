from random import random

class Neuron:
	
	"""
		# A class to create a neuron with the next properties:
			- An list of inputs
			- A list of weights
			- A activation function
			- A name for the activation function
			- A error value
	"""
	
	def __init__(self, nbInputs, nameFunction):
		
		"""
			# The constructor for the class Neuron that takes the following parameters:
				- nbInputs: a number of input
				- nameFunction: the name of the activation function
		"""
		
		self._inputsList = []
		self._weightList = []
		# Generate a list of weights
		for i in range(0, nbInputs):
			self._weigthList[i] = random()
		self._nameActivationFunction = nameFunction
		# Define the activation function thanks his name
		if (nameFunction == 'sigmoide'):
			self._activationFunction = sigmoide
		elif (nameFunction == 'hyperbolicTangente'):
			self._activationFunction = hyperbolicTangent
		elif (nameFunction == 'identity'):
			self._activationFunction = identity
		# Initialize error to 0
		self._error = 0