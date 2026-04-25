import pandas as pd

#read data from csv into data frame
df = pd.read_csv("servey.csv", encoding="UTF-8")
# df = pd.read_excel
# df = pd.read_json
# for large files we can read with the help of loops 
# if data is stored in a cloud platform than we can use gcsfs library
print(df)