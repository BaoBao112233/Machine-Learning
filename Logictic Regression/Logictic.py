import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataFrame = pd.read_csv('data_classification.csv', header=None)
# print(dataFrame)
Studied = dataFrame.values[:, 0]
Slept = dataFrame.values[:, 1]

# plt.scatter(Studied, Slept, marker='o')
# plt.show()

true_x = []
true_y = []
false_x = []
false_y = []

for item in dataFrame.values:
    if item[2] == 1.:
        true_x.append(item[0])
        true_y.append(item[1])
    else:
        false_x.append(item[0])
        false_y.append(item[1])

plt.scatter(true_x, true_y, marker='o', c='b')
plt.scatter(false_x, false_y, marker='x', c='r')
# plt.show()

def sigmoid(z):
    return 1/(1 + np.exp(-z))

def Boundary(p): # Ranh giới
    if p >= 0.5:
        return 1
    else:
        return 0