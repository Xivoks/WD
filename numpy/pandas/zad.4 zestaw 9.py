import pandas as pd
import numpy as np
from sklearn import datasets
import matplotlib.pyplot as plt

iris = datasets.load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
plt.scatter(df['sepal length (cm)'], df['sepal width (cm)'], c=iris.target)

plt.show()
