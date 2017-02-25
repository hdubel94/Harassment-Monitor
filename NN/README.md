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

import network  
import random  

my_net = network.Network([2, 3, 1])  
iterations = 10000  
step_size = 0.3  

input = [[0, 0], [0, 1], [1, 0], [1, 1]]  
expected_output = [[0], [1], [1], [0]]  

for i in range(iterations):  
	index = random.randint(0, 3)  
	my_net.train(input[index], expected_output[index], step_size)  

print(my_net.eval([0, 0]))  
print(my_net.eval([0, 1]))  
print(my_net.eval([1, 0]))  
print(my_net.eval([1, 1]))  

On my machine, running this code generated the following output:

[0.053809608683777314]  
[0.9422783350260181]  
[0.9423615769647524]  
[0.061911066848066174]  

While your output will not be exactly the same, the first and final values should be close to zero while the middle two values should be close to one. It is most effective to design your network with binary IOs and round the resulting output to make decisions.
