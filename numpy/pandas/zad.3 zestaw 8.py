import pandas as pd
import numpy as np
import datetime


def unikalne(df):
    print(df[1].unique())


def najwyzsze_zamowienie(df):
    p = df.sort_values('Utarg', ascending=False)
    print(p[:5])


def ile_zamowil(df):
    p = df.groupby(["Sprzedawca"]).agg({"idZamowienia": ['count']})
    print(p)


def ile_zamowil_kraj(df):
    p = df.groupby(["Kraj"]).agg({"idZamowienia": ['count']})
    print(p)


def suma_2005(df):
    p = df.copy()
    p['year'] = pd.DatetimeIndex(p['Data zamowienia']).year
    p = p.groupby(["year", 'Kraj']).agg({"idZamowienia": ['count']})
    print(p.index.values[5], p.values[5])


def srednia_2004(df):
    p = df.copy()
    p['year'] = pd.DatetimeIndex(p['Data zamowienia']).year
    p = p[p['year'] == 2004].agg({"Utarg": ['mean']})
    print(2004, p.values)


def zapisz_srednia(df):
    p = df.copy()
    p['Rok'] = pd.DatetimeIndex(p['Data zamowienia']).year
    dwa_tysiace_czwarty = p[p["Rok"] == 2004].copy()
    dwa_tysiace_czwarty = dwa_tysiace_czwarty.drop(['Rok'], axis=1)
    dwa_tysiace_czwarty.to_csv('zamowienia_2004.csv', header=True, index=False)
    dwa_tysiace_piaty = p[p["Rok"] == 2005].copy()
    dwa_tysiace_piaty = dwa_tysiace_piaty.drop(['Rok'], axis=1)
    dwa_tysiace_piaty.to_csv('zamowienia_2005.csv', header=True, index=False)


df = pd.read_csv('pandas/zamowienia.csv', header=0, delimiter=";")
# print(df.head)
# unikalne(df)
# najwyzsze_zamowienie(df)
# ile_zamowil(df)
# ile_zamowil_kraj(df)
# suma_2005(df)
# srednia_2004(df)
# zapisz_srednia(df)
