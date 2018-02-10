from Neuron import Neuron

######################################################################
#
#	Author: Developpix
#	Version: 0.1
#	License: GPLv3
#
#	File content: The layer's class
#
######################################################################

class Layer:
	
	"""
		# A class to create a layer which contains neurons. Layer has one property:
			- nbNeurons : the number of neurons contained
	"""
	
	def __init__(self, numberOfNeurons, numberOfNeuronsInTheLayerBefore, nameFunction):
		
		"""
			# The constructor of the layer's class, which takes 3 parameters:
				- numberOfNeurons : the number of the neurons contained in the layer
				- numberOfNeuronsInTheLayerBefore : the number of the neurons contained in the layer before
				- nameFunction : the name of the activation function
		"""
		
		self._nbNeurons = numberOfNeurons
		self._neuronsList = []
		for i in range(0, numberOfNeurons):
			self._neuronsList.append(Neuron(numberOfNeuronsInTheLayerBefore, nameFunction))
	
	"""
		# Getters and setters
	"""
	
	def get_neuronsList(self):
		return self._neuronsList
	
	def get_Neuron(self, number):
		return self._neuronsList[number]
	
	def toString(self):
		layerString = '------------------------- Layer -------------------------\n'
		for neuron in self._neuronsList:
			layerString += neuron.toString()
		return layerString
		