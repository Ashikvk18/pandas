import pandas as pd
data1 = {
   "Time": pd.to_datetime([
        "2024-01-01",
        "2024-01-02",
        "2024-01-03",
        "2024-01-04",
        "2024-01-05"
    ]),
    "Value": [910, None, 307, None, 502]
}
print(data1)
df = pd.DataFrame(data1)
print(df)

print ("after interpolation")

df["Value"] = df["Value"].interpolate(method="time")
print(df)

