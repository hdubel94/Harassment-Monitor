import input_handler
import network
import network_metadata
import random
import training_data

network_structure = [100, 50, 1]
net = network.Network(network_structure)
step_size = 0.3

net.layers = network_metadata.layers
net.biases = network_metadata.biases
net.weights = network_metadata.weights

harassment = training_data.harassment
not_harassment = training_data.not_harassment

# Train random training data value n times and overwrite network metadata
def train(n):
	for i in range(n):
		harassment_index = random.randint(0, 1)
		if harassment_index == 1:
			training_index = random.randint(0, len(harassment) - 1)
			current_input = input_handler.phrase_to_hash(harassment[training_index])
			net.train(current_input, [1], step_size)
		else:
			training_index = random.randint(0, len(not_harassment) - 1)
			current_input = input_handler.phrase_to_hash(not_harassment[training_index])
			net.train(current_input, [0], step_size)
	f = open('network_metadata.py', 'w')
	f.write('layers = ' + str(net.layers) + '\n')
	f.write('biases = ' + str(net.biases) + '\n')
	f.write('weights = ' + str(net.weights) + '\n')
	f.close()
