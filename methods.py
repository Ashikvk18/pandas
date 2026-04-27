import pandas as pd
data1 = {
    "Time": [1, 2, 3, 4, 5],
    "Value": [10, None, 30, None, 50]
}
print(data1)
df = pd.DataFrame(data1)
print(df)


