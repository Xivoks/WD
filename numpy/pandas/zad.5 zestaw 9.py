import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("pandas/zamowienia.csv", header=0, delimiter=";")
p = df.groupby(['Sprzedawca']).agg({"idZamowienia": ['count']})
wykres = p.plot.bar()
wykres.legend()
plt.show()
