import pandas as pd
import numpy as np
import xlrd
import openpyxl
import matplotlib.pyplot as plt

df = pd.read_excel(pd.ExcelFile("pandas/imiona.xlsx"))
p = df.groupby(['Plec']).agg({'Liczba': ['sum']})
print(p)
wykres = p.plot.bar()
wykres.set_ylabel('mln')
wykres.legend()
plt.show()
