# from numpy import dtype

from dateutil import rrule
from datetime import datetime, timedelta
import pandas as pd

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_json('test.json')

## estraggo "transactionsLog" dal json e popolo il dataframe 
df = (df["transactionsLog"].apply(pd.Series))

## rimuovo le colonne inutili dal dataframe
df = df.drop(columns=['Id','Token','ResCode','ResDescription','Levels','User'])

# let's examine the types of the column labels
# print(all(isinstance(column, str) for column in df.columns))

# # divido la colonna "Date" in due colonne separate "Date" e "Time"
df['Time'] = pd.to_datetime(df['Date']).dt.time
df['Date'] = pd.to_datetime(df['Date']).dt.date

## aggiungo una nuova colonna boolean "IsChangeNotDispensed" per i pagamenti completati e non in errore
df['IsChangeNotDispensed'] = ((df['NotDispensed'] > 0) & ((df['TransactionCode'] == 'PAY') | (df['TransactionCode'] == 'WITHDRAWAL')))

## Filter data between two dates # Soluzione alternativa: filtered_df = (df[df['Date'].between(datestart, dateend)])
datestart = pd.Timestamp("2021-12-09")
dateend = pd.Timestamp("2021-12-09" )
filtered_date_df = df.loc[(df['Date'] >= datestart) & (df['Date'] <= dateend) & (df['TransactionCode'] == 'PAY')]


# count = (filtered_date_df['TransactionCode'].value_counts().to_dict())
# print(count)

print(filtered_date_df.head())
print(filtered_date_df.dtypes)
