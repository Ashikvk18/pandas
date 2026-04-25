import pandas as pd

data = {
    "Name" : ["Amit", "Ashik", "Rakin"],
    "Age" : [10,20,30],
    "City" : ["Texas", "California", "London"]
}

df = pd.DataFrame(data)
print(df)