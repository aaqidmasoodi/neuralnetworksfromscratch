import numpy as np



inputs = [
    [1,2,3,2.5],
    [2.6,1.8,0.6,3.4],
    [8,2.4,1,9],
]
# weights = [0.2, 0.8, -0.5, 1.0]
# bias = 2
weights = [

    [1.4,2.6,1.0,5.1],
    [2.4,-4.1,4.1,8.2],
    [0.5, 6.1, -0.6, 1.1],

]

biases = [2.0, 4.1, 5.1]



output = np.dot(inputs, np.array(weights).T) + biases

print(output)
