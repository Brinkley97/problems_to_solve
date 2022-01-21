#perceptron algorithm has "W[0] += X[i][0]*learn_rate" & I am confused on the "X[i][0]"
#so I'll create my own algorithm to understand how it's working
#w3 schools example of an array in python

cars = ["Ford", "Volvo", "BMW"]
for i in range(0, len(cars)) :
    valueAlone = cars
    valueWithIndex = cars[i]
    valueWithSpecificIndex = cars[0]
    #[array name][index][value or #] => at this specific index, pull this value
    valueWithIndexAndSpecificIndex = cars[i][0]
    valueWithIndexAndSpecificIndex2 = cars[i][1]
    #can also be moved outside the for loop
print("value alone = ", valueAlone)
print("value with index = ", valueWithIndex)
print("value with specific index = ", valueWithSpecificIndex)
print("value with index & specific index = ", valueWithIndexAndSpecificIndex)
print("value with index & specific index = ", valueWithIndexAndSpecificIndex2)
