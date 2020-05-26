import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_excel('pandas/imiona.xlsx')
df_np = np.array(df)
q = df.groupby(['Plec']).agg({"Liczba": ["sum"]})
k = q.values[0][0]
m = q.values[1][0]
etykiety = ["K", "M"]
wartosci = [k, m]
plt.subplot(1, 3, 1)
plt.bar(etykiety, wartosci)
plt.ylabel('Ilość narodzin[mln]')
plt.xlabel('Płeć')

x_min = (df.agg({"Rok": ["min"]})).values[0][0]
x_max = (df.agg({"Rok": ["max"]})).values[0][0]
mezczyzn = df[df["Plec"] == 'M'].groupby(['Rok']).agg({"Liczba": ["sum"]})
kobiety = df[df["Plec"] == 'K'].groupby(['Rok']).agg({"Liczba": ["sum"]})
x = np.linspace(x_min, x_max, 18)
y1 = [mezczyzn.values[z][0] for z in range(18)]
y2 = [kobiety.values[c][0] for c in range(18)]
plt.subplot(1, 3, 2)
plt.plot(x, y1, label='M')
plt.plot(x, y2, label='K')
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()

x_mina = (df.agg({"Rok": ["min"]})).values[0][0]
x_maxa = (df.agg({"Rok": ["max"]})).values[0][0]
mezczyzna = (df.groupby(['Rok'])).agg({"Liczba": ["sum"]})
x = np.linspace(x_mina, x_maxa, 18)
y1 = [mezczyzna.values[z][0] for z in range(18)]
plt.subplot(1, 3, 3)
plt.bar(x, y1, label='M')
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.show()
