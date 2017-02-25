import math
import random

# Using sigmoid function as activation
def sigmoid(x):
	return 1.0 / (1 + math.exp(-x))

# Derivative of sigmoid function
def sigmoid_prime(x):
	return sigmoid(x) * (1 - sigmoid(x))

# Network class
class Network():

	# Initializing network based on neuron structure
	def __init__(self, dimensions):
		self.layers = len(dimensions) - 1
		self.biases = []
		self.weights = []
		for index, size in enumerate(dimensions):
			if index > 0:
				self.biases.append([])
				for i in range(size):
					self.biases[-1].append(4 * random.random() - 2)
			if index < self.layers:
				self.weights.append([])
				for x in range(size):
					self.weights[-1].append([])
					for y in range(dimensions[index + 1]):
						self.weights[-1][-1].append(4 * random.random() - 2)

	# Forward propagation function that returns the output of the network
	def eval(self, input_values):
		feed_forward = self.evaluate(input_values)
		return feed_forward[0][-1]

	# Forward propagation function that returns all activation and z values
	def evaluate(self, input_values):
		activations = [input_values]
		zs = []
		for layer_index in range(self.layers):
			current_activations = activations[-1]
			activations.append([])
			zs.append([])
			for dest_node_index, dest_node in enumerate(self.biases[layer_index]):
				current_sum = 0
				for weight_index, weight in enumerate(self.weights[layer_index]):
					current_sum += current_activations[weight_index] * weight[dest_node_index]
				zs[-1].append(current_sum + dest_node)
				activations[-1].append(sigmoid(zs[-1][-1]))
		return [activations, zs]

	# Training the network with input, expected output, and step size
	def train(self, input_values, output_values, eta):
		feed_forward = self.evaluate(input_values)
		activations = feed_forward[0]
		zs = feed_forward[1]
		delta_bias = [[]]
		delta_weight = [[]]
		for output_index, expected_value in enumerate(output_values):
			delta_bias[0].append((activations[-1][output_index] - expected_value) * sigmoid_prime(zs[-1][output_index]))
		for activation in activations[-2]:
			delta_weight[0].append([])
			for delta in delta_bias[0]:
				delta_weight[0][-1].append(delta * activation)
		for layer_index in range(self.layers - 2, -1, -1):
			delta_bias.insert(0, [])
			delta_weight.insert(0, [])
			for weight_index, weight in enumerate(self.weights[layer_index + 1]):
				current_sum = 0
				for i, w in enumerate(weight):
					current_sum += w * delta_bias[1][i]
				delta_bias[0].append(current_sum * sigmoid_prime(zs[layer_index][weight_index]))
			for activation in activations[layer_index]:
				delta_weight[0].append([])
				for delta in delta_bias[0]:
					delta_weight[0][-1].append(delta * activation)
		for layer_index in range(self.layers):
			for bias_index, bias in enumerate(self.biases[layer_index]):
				self.biases[layer_index][bias_index] = bias - eta * delta_bias[layer_index][bias_index]
			for weight_index, weight in enumerate(self.weights[layer_index]):
				for w_index, w in enumerate(weight):
					self.weights[layer_index][weight_index][w_index] = w - eta * delta_weight[layer_index][weight_index][w_index]
