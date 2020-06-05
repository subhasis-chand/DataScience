from sklearn.tree import DecisionTreeClassifier
import numpy as np
import sklearn
from sklearn.model_selection import train_test_split
from sklearn import tree
import matplotlib.pyplot as plt

data = np.genfromtxt('./breastCancerDataWisconsin.csv', delimiter=',')  # loading of data
data = data[1:, 1:] # Cleaning of data
opData = data[:, 0] # Extracting output
ipData = data[:, 1:5]   #extracting input
# Splitting the data
ipTrain, ipTest, opTrain, opTest = train_test_split(ipData, opData, test_size=0.2, shuffle=True)

model = DecisionTreeClassifier()
model.fit(ipTrain, opTrain)

opPred = model.predict(ipTest)

tree.plot_tree(model) 
plt.show()