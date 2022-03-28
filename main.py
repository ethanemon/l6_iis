#!/usr/bin/python
from numpy import exp, array, random, dot

training_set_inputs = array([[1, 1, 0], [0, 0, 1], [0, 0, 0], [0, 0, 1]])
training_set_outputs = array([[0, 0, 1, 1]]).T
random.seed(1)
synaptic_weights = 2 * random.random((3, 1)) - 1

for iteration in range(10000):
    output = 1 / (1 + exp(-(dot(training_set_inputs, synaptic_weights))))
    synaptic_weights += dot(training_set_inputs.T, (training_set_outputs - output) *
                            output * (1 - output))

print("Учитывая ситуацию [0, 1, 0] -> ?: ")
print(1 / (1 + exp(-(dot(array([0, 1, 0]), synaptic_weights)))))
