from random import random

######################################################################
#
#	Author: Developpix
#	Version: 0.1
#	License: GPLv3
#
#	File content: The neuron's class
#
######################################################################

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
		self._lastWeightList = []
		# Generate a list of weights
		for i in range(0, nbInputs):
			self._weigthList[i] = random()
		self._lastWeightList = self._weightList
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
	
	"""
		# Define getters and setters
	"""
	
	def get_inputsList(self):
		return self._inputsList
	
	def set_inputsList(self, newInputs):
		self._inputsList = newInputs
	
	def get_weightList(self):
		return self._weightList
		
	def get_lastWeightList(self):
		return self._lastWeightList
	
	def set_weightList(self, newWeights):
		self._lastWeightList = self._weightList
		self._weightList = newWeights
	
	def get_error(self):
		return self._error
	
	def set_error(self, newError):
		self._error = newError
	
	def get_nameActivationFunction(self):
		return self._nameActivationFunction
	
	def set_activationFunction(self, nameNewFunction):
		self._nameActivationFunction = nameNewFunction
		# Define the activation function thanks his new name
		if (nameNewFunction == 'sigmoide'):
			self._activationFunction = sigmoide
		elif (nameNewFunction == 'hyperbolicTangente'):
			self._activationFunction = hyperbolicTangent
		elif (nameNewFunction == 'identity'):
			self._activationFunction = identity
	
	def get_output(self):
		somme = 0
		for i in range(0, len(self._weightList)):
			somme += self._inputsList[i] * self._weightList[i]
		return self._activationFunction(somme)
	
	def toString(self):
		
		"""
			# Function to transform the neuron in a string
		"""
		
		chaine = '------- Neuron -------\n'
		chaine += 'Activation function : ' + self._nameActivationFunction + '\n'
		chaine += 'Inputs : ' + str(self._inputsList) + '\n'
		chaine += 'Weights : ' + str(self._weightList) + '\n'
		chaine += 'Output : ' + str(self.get_output()) + '\n'
		chaine += 'Error : ' + str(self._error) + '\n'
		return chaine