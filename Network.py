from Layer import Layer

######################################################################
#
#	Author: Developpix
#	Version: 0.1
#	License: GPLv3
#
#	File content: The network's class
#
######################################################################

class Network:
	
	"""
		# A class to create a neural network, with one property:
			- nbLayers : the number of layers contained in the neural network
	"""
	
	def __init__(self, numberOfLayers, listOfNumberOfNeuronsPerLayer, nameFunction):
		
		"""
			# The constructor for the network's class, which takes 3 paramaters:
				- numberOfLayers: the number of layers contained in the neural network
				- listOfNumberOfNeuronsPerLayer: a list that contains the number of neurons per layer
				- nameFunction: the name of the activation funtion
		"""
		
		self._nbLayers = numberOfLayers
		self._layersList = []
		for i in range(0, numberOfLayers):
			if (i > 0):
				inputsNumberForNeurons = listOfNumberOfNeuronsPerLayer[i-1]
			else:
				inputsNumberForNeurons = 1
			self._layersList.append(Layer(listOfNumberOfNeuronsPerLayer[i], inputsNumberForNeurons, nameFunction))
	
	