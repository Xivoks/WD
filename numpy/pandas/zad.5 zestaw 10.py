import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets

iris = datasets.load_iris()
plt.scatter(iris.data[:, 0], iris.data[:, 1],
            c=iris.target, s=abs(iris.data[:, 0]-iris.data[:, 1]))
plt.xlabel('sepal length')
plt.ylabel('sepal width')
plt.show()
