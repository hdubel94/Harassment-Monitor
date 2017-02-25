This file will serve as basic documentation for network.py.

Importing the file (ensure that you are in the same directory as network.py):

import network

Creating a three layer network with two input neurons, three hidden layer neurons, and one output layer neuron:

my_net = network.Network([2, 3, 1])

The network can have any number of layers (at least three for back propagation) and any number of neurons per layer (at least one). The first value is assumed to be the input layer and the final value is assumed to be the output layer. Anything in between will be a hidden layer.

Training the network with input values, expected output values, and step size value:

my_net.train([0, 1], [1], 0.3)

Input and output values must be contained within a list, even if it is a single value. This example trains a zero and one to the input neurons and a one should be expected as the output value. A step size of 0.3 is used in the training.

Checking the output values upon forward propagation:

network_output = my_net.eval([0, 1])

In a well trained network, the resulting value of network_output should be close to [1]. Keep in mind, the return value is still a list, even if there is only one neuron in the output layer.

Here is some example code for creating a neural network and training it to act as a XOR gate:

import network__
import random__

my_net = network.Network([2, 3, 1])__
iterations = 10000__
step_size = 0.3__

input = [[0, 0], [0, 1], [1, 0], [1, 1]]__
expected_output = [[0], [1], [1], [0]]__

for i in range(iterations):__
	index = random.randint(0, 3)__
	my_net.train(input[index], expected_output[index], step_size)__

print(my_net.eval([0, 0]))__
print(my_net.eval([0, 1]))__
print(my_net.eval([1, 0]))__
print(my_net.eval([1, 1]))__

On my machine, running this code generated the following output:

[0.053809608683777314]__
[0.9422783350260181]__
[0.9423615769647524]__
[0.061911066848066174]__

While your output will not be exactly the same, the first and final values should be close to zero while the middle two values should be close to one. It is most effective to design your network with binary IOs and round the resulting output to make decisions.
