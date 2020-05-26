import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('pandas/zamowienia.csv', header=0, delimiter=";")
df_np = np.array(df)
dane = df.groupby(['Sprzedawca']).agg({"idZamowienia": ["count"]})

wedges, texts, autotexts = plt.pie(dane.values, labels=dane.index.values,
                                   autopct=lambda pct: "{:.1f}%".format(pct), textprops=dict(color="black"))
plt.setp(autotexts, size=14, weight="bold")
plt.title("Pierwsza wersja wykresu")
plt.legend(title='Zawodnicy')
plt.show()
