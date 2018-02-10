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
		self._neurons = []
		for i in range(0, numberOfNeurons):
			neurons.append(Neuron(numberOfNeuronsInTheLayerBefore, nameFunction))
	
	