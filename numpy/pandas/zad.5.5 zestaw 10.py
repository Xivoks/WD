import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import datasets

iris = datasets.load_iris()
plt.scatter(iris.data[:, 0], iris.data[:, 1], c=iris.target, s=5)
plt.show()
