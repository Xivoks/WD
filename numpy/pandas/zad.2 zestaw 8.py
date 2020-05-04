import pandas as pd
import numpy as np
import xlrd
import openpyxl


def suma(df):
    p = df.groupby(["Rok"]).agg({"Liczba": ['sum']})
    print(p[['Liczba'] > 1000])


def moje_imie(df):
    print(df[df['Imie'] == "JAN"])


def suma_caly(df):
    p = df.agg({"Liczba": ['sum']})
    print(p)


def suma_okres(df):
    p = df[(df['Rok'] >= 2000) & (df['Rok'] <= 2005)].agg({"Liczba": ['sum']})
    print(p)


def plec(df):
    m = df[df["Plec"] == 'M'].agg({"Liczba": ["sum"]})
    d = df[df["Plec"] == 'K'].agg({"Liczba": ["sum"]})
    print(m)
    print(d)


def imie(df):
    p = df.sort_values("Liczba", ascending=False).groupby(['Rok', "Plec"])
    for i, z in enumerate(p, 1):
        print(f"{z[0]}")
        print(f"{z[1].iloc[[0],[1]].values[0][0]}",
              f"{z[1].iloc[[0],[2]].values[0][0]}")


def popularne_imie(df):
    k = df[df['Plec'] == 'K']
    k_max = df[df['Plec'] == 'K'].max()
    print(k[(k['Liczba'] == k_max['Liczba'])])
    m = df[df['Plec'] == 'M']
    m_max = df[df['Plec'] == 'M'].max()
    print(m[(m['Liczba'] == m_max['Liczba'])])


xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx, 'Arkusz1')
# print(df)
# suma(df)
# moje_imie(df)
# suma_caly(df)
# plec(df)
imie(df)
# popularne_imie(df)
