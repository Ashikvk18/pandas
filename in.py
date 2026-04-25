import pandas as pd

df = pd.read_csv("servey.csv")
print(df.info())

dm = pd.read_csv("data.csv")
print(dm.info())