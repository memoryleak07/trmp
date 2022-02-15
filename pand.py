# from numpy import dtype
import pandas as pd

df = pd.read_json('test.json')

print(df.head(5))

#estraggo "transactionsLog" dal json e popolo il dataframe 
df = (df["transactionsLog"].apply(pd.Series))
print(df.head(5))

#rimuovo le colonne inutili dal dataframe
df = df.drop(columns=['Token','ResCode','ResDescription','Levels','User'])
print(df.head(5))

# divido la colonna "Date" in due colonne separate "Date" e "Time"
df['Time'] = pd.to_datetime(df['Date']).dt.time
df['Date'] = pd.to_datetime(df['Date']).dt.date
print(df.head(5))

#aggiungo una nuova colonna boolean "IsChangeNotDispensed" per i pagamenti completati e non in errore
df['IsChangeNotDispensed'] = ((df['NotDispensed'] > 0) & (df['TransactionStatus'] == 'COMPLETED') & (df['TransactionCode'] == 'PAY'))
print(df.head(5))
