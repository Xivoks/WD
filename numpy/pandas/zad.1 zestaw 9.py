import pandas as pd
import numpy as np
import xlrd
import openpyxl
import matplotlib.pyplot as plt

df = pd.read_excel(pd.ExcelFile("pandas/imiona.xlsx"))
p = df.groupby(['Rok']).agg({'Liczba': ['sum']})
p.plot(xticks=p.index.values)
plt.legend()
plt.show()
