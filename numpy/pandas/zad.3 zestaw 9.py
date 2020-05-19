import pandas as pd
import numpy as np
import xlrd
import openpyxl
import matplotlib.pyplot as plt

df = pd.read_excel(pd.ExcelFile("pandas/imiona.xlsx"))
pd = df.agg({"Rok": ['max']})
p = df[(df["Rok"] <= pd.values[0][0]) & (df["Rok"] > pd.values[0][0]-5)]
pf = p.groupby(['Plec']).agg({'Liczba': ['sum']})
print(pf)
wykres = pf.plot.pie(subplots=True, autopct='%.2f%%',
                     fontsize=10, figsize=(6, 6))
plt.show()
