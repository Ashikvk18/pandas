import pandas as pd

#read data from csv into data frame
df = pd.read_csv("servey.csv", encoding="UTF-8")
print(df)