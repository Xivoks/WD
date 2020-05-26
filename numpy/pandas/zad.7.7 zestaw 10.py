import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_excel('pandas/imiona.xlsx')
df_np = np.array(df)
x_min = (df.agg({"Rok": ["min"]})).values[0][0]
x_max = (df.agg({"Rok": ["max"]})).values[0][0]
mezczyzn = df[df["Plec"] == 'M'].groupby(['Rok']).agg({"Liczba": ["sum"]})
kobiety = df[df["Plec"] == 'K'].groupby(['Rok']).agg({"Liczba": ["sum"]})
x = np.linspace(x_min, x_max, 18)
y1 = [mezczyzn.values[z][0] for z in range(18)]
y2 = [kobiety.values[c][0] for c in range(18)]
width = 0.30
plt.bar(x, y1, width, color="blue", label="M")
plt.bar(x, y2, width, color="red", bottom=y1, label="K")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.show()
