import numpy as np
np.random.seed(0)


X = [[1,2,3,2.5],
    [2.6,1.8,0.6,3.4],
    [8,2.4,1,9]]





class LayerDense:

    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.1 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))
    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases


l1 = LayerDense(4,5)
l2 = LayerDense(5,2)



l1.forward(X)
l2.forward(l1.output)
print(l2.output)
