inputs = [1.8, 2.1, 4, 1]

weights = [

    [1.4,2.6,1.0,5.1],
    [2.4,-4.1,4.1,8.2],
    [0.5, 6.1, -0.6, 1.1],

]

biases = [2.0, 4.1, 5.1]


layer_output = []

for neuron_weights, neuron_bias in zip(weights, biases):
    neuron_outut = 0

    for neuron_input, neuron_weight in zip(inputs, neuron_weights):
        neuron_outut += neuron_input * neuron_weight

    neuron_outut += neuron_bias
    layer_output.append(neuron_outut)



print(layer_output)
