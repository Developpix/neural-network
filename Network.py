from Layer import Layer
from functions import *
import pickle

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
		self._listOfLessons = []
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
	
	def backpropagation(self, normalOutputs, learningRate, alpha):
		
		"""
			# The method for backpropagation
		"""
		
		# Calculation of the error of the neurons in the last layer
		# Check if the number of outputs is correct
		if (len(normalOutputs) == len(self.get_lastLayer().get_neuronsList())):
			
			
			for i in range(0, len(self.get_Layer(self._nbLayers-1).get_neuronsList())):
				
				# store the neuron i in a variable
				n = self.get_Layer(self._nbLayers-1).get_Neuron(i)
				
				# Create an int to store the total
				total = 0
				
				# Calculation of the total
				for j in range(0, len(n.get_weightList())):
					
					total += n.get_weightList()[j] * n.get_inputsList()[j]
				
				# Get the derived function
				if (n.get_nameActivationFunction() == 'sigmoide'):
					derivedFunction = derived_sigmoide
				elif (n.get_nameActivationFunction() == 'hyperbolicTangent'):
					derivedFunction = derived_hyperbolicTangent
				elif (n.get_nameActivationFunction() == 'identity'):
					derivedFunction = derived_identity
				
				# Calculation of neuron's error and set his error
				error = derivedFunction(total) * (normalOutputs[i] - n.get_output())
				n.set_error(error)
		else:
			print('Le nombre de résultats attendus ne correspond pas aux sorties de la dernière couche')
		
		# Disseminate the error backwards
		for i in range(1, self._nbLayers):
			
			# reverse the direction
			i = self._nbLayers - (i + 1)
			
			# Neurons in the layer n
			for j in range(0, len(self.get_Layer(i).get_neuronsList())):
				
				# Store the neuron in a variable
				n = self.get_Layer(i).get_Neuron(j)
				
				# Create an int to store the total
				total = 0
				
				# Neurons in the layer n+1
				for k in range(0, len(self.get_Layer(i+1).get_neuronsList())):
					
					upperNeuron = self.get_Layer(i+1).get_Neuron(k)
					total += upperNeuron.get_weightList()[j] * upperNeuron.get_error()
				
				# Create an int to store the total of inputs
				inputsTotal = 0
				
				# Calculation of the total of inputs
				for k in range(0, len(n.get_weightList())):
					
					inputsTotal += n.get_weightList()[k] * n.get_inputsList()[k]
				
				# Get the derived function
				if (n.get_nameActivationFunction() == 'sigmoide'):
					derivedFunction = derived_sigmoide
				elif (n.get_nameActivationFunction() == 'hyperbolicTangent'):
					derivedFunction = derived_hyperbolicTangent
				elif (n.get_nameActivationFunction() == 'identity'):
					derivedFunction = derived_identity
				
				# Calculation of neuron's error
				error = derivedFunction(inputsTotal) * total
				n.set_error(error)
		
		# Update weight thanks to inertia
		for i in range(0, self._nbLayers):
			
			# Get neurons in the layer
			for j in range(0, len(self.get_Layer(i).get_neuronsList())):
				
				# Store the neuron in a variable
				n = self.get_Layer(i).get_Neuron(j)
				
				# Create a variable to store the new list of weight for the neuron
				newWeightList = []
				
				# Get the new list of weight for the neuron
				for k in range(0, len(n.get_weightList())):
					
					newWeightList.append(n.get_lastWeightList()[k] + (alpha * learningRate * n.get_error() * n.get_inputsList()[k]) + ((1 - alpha) * (n.get_weightList()[k] - n.get_lastWeightList()[k])))
				
				# Set the new list of weight
				n.set_weightList(newWeightList)
	
	def learn(self, inputs, normalOutputs, learningRate, tolerableError, alpha):
		
		"""
			# A method thanks to that the network can learn
		"""
		
		# Check if the network don't know the inputs
		if ((inputs, normalOutputs) not in self._listOfLessons):
			
			# Add in inputs and normalOutputs to the list of lessons
			self._listOfLessons.append((inputs, normalOutputs))
		
		knowAll = False
		
		while (knowAll == False):
			
			knowAll = True
			
			# Browse list of lessons
			for i in range(0, len(self._listOfLessons)):
				
				inputsList = self._listOfLessons[i][0]
				normalOutputsList = self._listOfLessons[i][1]
				
				self.propagation(inputsList)
				
				networkOutputsList = []
				
				know = True
				
				# Neurons in the last layer 
				for j in range(0, len(self.get_lastLayer().get_neuronsList())):
					
					n = self.get_lastLayer().get_Neuron(j)
					
					networkOutputsList.append(n.get_output())
					
					if (n.get_output() < (normalOutputsList[j] - tolerableError) or n.get_output() > (normalOutputsList[j] + tolerableError)):
						
						know = False
				
				if (know == False):
					
					knowAll = False
					
					while (know == False):
						
						know = True
						
						# We do a backpropagation and a propagation to check if there is still a error
						self.backpropagation(normalOutputsList, learningRate, alpha)
						self.propagation(inputsList)
						
						networkOutputsList2 = []
						
						# Neurons in the last layer
						for j in range(0, len(self.get_lastLayer().get_neuronsList())):
							
							n = self.get_lastLayer().get_Neuron(j)
							
							networkOutputsList2.append(n.get_output())
							
							if (n.get_output() < (normalOutputsList[j] - tolerableError) or n.get_output() > (normalOutputsList[j] + tolerableError)):
								
								know = False
	
	def save(self, fileName):
		
		"""
			# A method to save the network in a file
		"""
		
		with open(fileName, 'wb') as saveFile:
			data = pickle.Pickler(saveFile)
			data.dump(self)
			saveFile.close()
	
	def load(self, fileName):
		
		"""
			# Load a network that have been saved in a file
		"""
		
		with open(fileName, 'rb') as saveFile:
			data = pickle.Unpickler(saveFile)
			n = data.load()
			saveFile.close()
		
		self._nbLayers = n._nbLayers
		self._listOfLessons = n._listOfLessons
		self._layersList = n._layersList