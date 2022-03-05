import numpy as np

import scipy.special

class NeuralNetwork:
    def __init__(self, inputnodes, hiddennodes, outputnodes):
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes

        self.wih = np.random.normal(0.0, pow(self.hnodes, -0.5), (self.hnodes, self.inodes))
        self.who = np.random.normal(0.0, pow(self.onodes, -0.5), (self.onodes, self.hnodes))

        self.activation_function = lambda x: scipy.special.expit(x)

    def train(self, input_list, targets_list, learning_rate):
        inputs = np.array(input_list, ndmin=2).T
        targets = np.array(targets_list, ndmin=2).T

        hidden_layer_in = np.dot(self.wih, inputs)
        hidden_layer_out = self.activation_function(hidden_layer_in)

        output_layer_in = np.dot(self.who, hidden_layer_out)
        output_layer_out = self.activation_function(output_layer_in)

        output_error = targets - output_layer_out
        hidden_error = np.dot(self.who.T, output_error)

        self.who += learning_rate*np.dot(output_error*output_layer_out*(1.0-output_layer_out)),np.transepose(hidden_layer_out)
        self.wih += learning_rate*np.dot(hidden_error*hidden_layer_out*(1.0-hidden_layer_out)),np.transepose(inputs)

    def query(self, inputs_list):
        inputs = np.array(inputs_list, ndmin=2).T
        hidden_layer_in = np.dot(self.wih, inputs)
        hidden_layer_out = self.activation_function(hidden_layer_in)
        output_layer_in = np.dot(self.who,hidden_layer_out)
        output_layer_out = self.activation_function(output_layer_in)

        return output_layer_out

