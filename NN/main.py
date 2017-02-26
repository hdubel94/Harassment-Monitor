import input_handler
import network
import network_metadata

network_structure = [132, 25, 1]
net = network.Network(network_structure)
net_tolerance = 0.5

net.layers = network_metadata.layers
net.biases = network_metadata.biases
net.weights = network_metadata.weights

# Main function to check for harassment
def is_harassment(phrase):
	current_hash = input_handler.phrase_to_hash(phrase)
	network_output = net.eval(current_hash)
	if network_output[0] > net_tolerance:
		return 1
	else:
		return 0
