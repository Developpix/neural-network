from math import exp, tanh

######################################################################
#
#	Author: Developpix
#	Version: 0.1
#	License: GPLv3
#
#	File content: A list of activation function
#
######################################################################

# The sigmoide function with is derived
def sigmoide(val):
	return 1 / (1 + exp(-1 * val))

def derived_sigmoide(val):
	return sigmoide(val) * (1 - sigmoide(val))

# The heaviside function with is derived
# Don't use this function for a neuronal network because his derived is unknown in 0
def heaviside(val):
	if (val < 0):
		return 0
	else:
		return 1

def derived_heaviside(val):
	if (val != 0):
		return 0

# The identity function
def identity(val):
	return val

def derived_identity(val):
	return 1

# The hyperbolic tangent function
def hyperbolicTangent(val):
	return tanh(val)

def derived_hyperbolicTangent(val):
	return 1 - (tanh(val) * tanh(val))