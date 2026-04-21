import pandas as pd

#read data from csv into data frame
df = pd.read_csv("servey.csv", encoding="latin1")
print(df)