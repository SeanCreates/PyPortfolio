#ReadCSV
#Comma Separated Value - Plain Text Format For Storing Tabular Data
import pandas as pd
df = pd.read_csv('/Users/seaniceochieng/PycharmProjects/ML/PyPortfolio/Data/data.csv')
print(df.to_string())

#ALWAYS USE THE ABSOLUTE PATH
print(pd.options.display.max_rows)
pd.options.display.max_rows = 30
df = pd.read_csv('/Users/seaniceochieng/PycharmProjects/ML/PyPortfolio/Data/data.csv')
print(df)

df = pd.read_csv('/Users/seaniceochieng/PycharmProjects/ML/PyPortfolio/Data/data.csv')
print(df.head(5))
print(df.tail(10))
print(df.info())
#Null values - no entry
#164/169 non-null values means 5 with no values

print(df.describe())