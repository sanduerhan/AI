from math import e
import random
import numpy as np

with open('input') as f:
    w, h = [int(x) for x in next(f).split()]
    array = [[int(x) for x in line.split()] for line in f]

epoci = int(input("Introduceti nr de epoci: "))
rata_inv = float(input("Introduceti rata de invatare: "))
input_neurons = 2
hidden_neurons = 2
output_neurons = 1


def sigmoid(x):
    return 1 / (1 + e ** (-x))


def sigmoid_derivative(x):
    return x * (1.0 - x)


weight1 = np.random.uniform(low=-0.05, high=0.05, size=(input_neurons, hidden_neurons))
weight2 = np.random.uniform(low=-0.05, high=0.05, size=(output_neurons, hidden_neurons))
output1 = 0
output2 = 0
hidden_node1 = weight1[0]
hidden_node2 = weight1[1]
output_node = weight2[0]
error1 = 0
error2 = 0
output_error = 0


def forward_propagation(input_values):
    global output1, output2
    z1 = hidden_node1[0] * input_values[0] + hidden_node2[0] * input_values[1]      #weight*valorea de input
    z2 = hidden_node2[1] * input_values[0] + hidden_node2[1] * input_values[1]

    y1 = sigmoid(z1)    #aplicarea functiei de activare
    y2 = sigmoid(z2)
    output1 = y1
    output2 = y2
    #print(output1)
    #print(output2)
    output = output_node[0] * y1 + output_node[1] * y2
    y3 = sigmoid(output)        #outputul de la forwardpropagation pe neuronul de pe stratul de iesire

    return y3


# print(forward_propagation())

def back_propagation(y3, output_value):
    global error1, error2, output_error
    output_error = y3 - output_value        # y3 outputul retelei si output_value - targetul
    error1 = (output_node[0] * output_error) * output1 * (1-output1)
    error2 = (output_node[1] * output_error) * output2 * (1-output2)


def update_weights(input_values):
    global hidden_node1, hidden_node2,output_node
    hidden_node1[0] -= rata_inv * error1 * input_values[0]
    hidden_node1[1] -= rata_inv * error2 * input_values[1]
    hidden_node2[0] -= rata_inv * error1 * input_values[0]
    hidden_node2[1] -= rata_inv * error2 * input_values[1]
    output_node[0] = round(output_node[0]-rata_inv * output_error * output1,2)
    output_node[1] = round(output_node[1]-rata_inv * output_error * output2,2)


def train(rata_inv, epoci, array):
    for i in range(epoci):
        for index in range(h):
            input = [None] * 2
            for j in range(2):
                input[j] = array[index][j]
            output_value = array[index][2]
            y3 = forward_propagation(input)
            back_propagation(y3, output_value)
            update_weights(input)

def predict(input_values):
    output = forward_propagation(input_values)
    print(output)
    if output >= 0.4:
        return 1
    return 0

train(rata_inv, epoci, array)
for i in range(h):
    input_values = [None] * 2
    for j in range(2):
        input_values[j] = array[i][j]
    output_value = array[i][2]
    print("Inputul este: ", input_values)
    print("Reteaua a prezis: ", predict(input_values))
    print("Valoarea asteptata: ", output_value)