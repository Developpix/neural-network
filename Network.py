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
	
	"""
		# Getters and setters
	"""
	
	def get_layersList(self):
		return self._layersList
	
	def get_Layer(self, number):
		return self._layersList[number]
	
	def get_lastLayer(self):
		return self._layersList[self._nbLayers-1]
	
	def toString(self):
		
		"""
			# Method to transform the network in a string 
		"""
		
		networkString = '-------------------------- Network --------------------------\n'
		for i in range(0, self._nbLayers):
			networkString += self._layersList[i].toString()
		networkString += '-------------------------- End of network --------------------------\n'
		return networkString
	
	def propagation(self, inputs):
		
		"""
			# Method for propagation
		"""
		
		# Check if there is the correct number of inputs
		if (len(inputs) == len(self.get_Layer(0).get_neuronsList())):
			
			# Add the input for the neurons in the first layer
			for i in range(0, len(self.get_Layer(0).get_neuronsList())):
				
				self.get_Layer(0).get_Neuron(i).set_inputsList([inputs[i]])
		else:
			
			print('ERROR: The number of inputs is incorrect !')
		
		# Disseminate the information
		for i in range(1, self._nbLayers):
			
			# Create a table to store the outputs of the neurons in the layers before
			inputsList = []
			
			# Get the outputs of the neurons in the layer before
			for j in range(0, len(self.get_Layer(i-1).get_neuronsList())):
				
				inputsList.append(self.get_Layer(i-1).get_Neuron(j).get_output())
			
			# Add the outputs of the layer before to the inputs of the layer
			for j in range(0, len(self.get_Layer(i).get_neuronsList())):
				
				self.get_Layer(i).get_Neuron(j).set_inputsList(inputsList)
	