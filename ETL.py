import pandas as pd
import numpy as np

def rentas():
    rentas = 'rentas.csv'
    return pd.read_csv(rentas)

def renta():
    renta = 'renta.csv'
    return pd.read_csv(renta)

def df1(renta = renta(),rentas =rentas()):
    precio_renta_MXN = renta['info'].str.split(expand=True)
    precio_renta_MXN.rename(columns={1: 'USD_MXN', 0: 'price'}, inplace=True)
    USD_MXN = precio_renta_MXN['USD_MXN']
    precio_renta = precio_renta_MXN['price'].str.split('$', n=2, expand=True)
    precio_renta = precio_renta.drop(columns=[0])
    precio_renta.rename(columns={1: 'price'}, inplace=True)
    signo = precio_renta.assign(signo='$')
    signo = signo.drop(columns=['price'])
    m2_a_l_estac = renta['m2_a_l_estac'].str.split('\n', n=2, expand=True)
    m2_a_l_estac.rename(columns={1: 'm2', 0: 'banos'}, inplace=True)
    direccion = renta['direccion']
    return pd.concat([signo, precio_renta, USD_MXN, m2_a_l_estac, direccion], axis=1)

def df2(renta = renta(),rentas =rentas()):
    price = rentas['info'].str.split('\n', n=2,expand=True).drop(columns=[2, 1])
    direccion = rentas['direccion']
    #signo = price.assign(signo='$').drop(columns=[0])
    price = price[0].str.split('MN', expand=True).drop(columns=[0])
    price.rename(columns={1: 'price'}, inplace=True)
    m2 = rentas['m2_a_l_estac'].str.split('\n', n=2, expand=True)
    m2.rename(columns={0: 'm2', 2: 'banos'}, inplace=True)
    m2 = m2.drop(columns=[1])
    return pd.concat([price, m2, direccion], axis=1)

def conact(df1 = df1(), df2=df2()):
    return pd.concat([df1, df2], axis=0)

df = conact()
if __name__ == '__main__':
    print(df)