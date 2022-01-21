###
#Count
###

import numpy as np

line = np.array([3,4,-10])
learningRate = 0.1
points = np.array([1,1])
bias = 1

adjustedPoints = learningRate * points * bias
newLine = line + adjustedPoints
