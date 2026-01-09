from datetime import datetime
import pandas as pd

df = pd.read_csv('/Users/seaniceochieng/PycharmProjects/ML/PyPortfolio/Data/Sheet1.csv')
# Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])
#df.dropna(inplace=True)
#df.fillna({"Calories" : 130.0 , "Date": "2020/12/01"}, inplace = True)
x = df["Calories"].mean()
df.fillna({"Calories": x , "Date": "2020/12/01"}, inplace = True)
x = df["Calories"].median()

print(df.to_string())