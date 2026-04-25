import pandas as pd

data = {
    "Name" : ["Amit", "Ashik", "Rakin"],
    "Age" : [10,20,30],
    "City" : ["Texas", "California", "London"]
}

df = pd.DataFrame(data)
print(df)

df.to_csv("data.csv", index=False)

df.to_excel("data.xlsx", index=False)

df.to_json("data.json", index=False)