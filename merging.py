import pandas as pd
df_customers = pd.DataFrame({
    "CustomerID": [1, 2, 3, 4, 5],
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Eve"],
    "City": ["New York", "London", "Paris", "Tokyo", "Berlin"]
})
df_orders = pd.DataFrame({
    "OrderID": [101, 102, 103, 104, 105],
    "CustomerID": [1, 2, 1, 3, 2],
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones"]
})

df_merged = pd.merge(df_customers, df_orders, on="CustomerID", how="inner")
print(df_merged)
print("\n")

df_left = pd.merge(df_customers, df_orders, on="CustomerID", how="left")
print(df_left)
print("\n")

df_right = pd.merge(df_customers, df_orders, on="CustomerID", how="right")
print(df_right)
print("\n")

df_outer = pd.merge(df_customers, df_orders, on="CustomerID", how="outer")
print(df_outer)
print("\n")

df_cross = pd.merge(df_customers, df_orders, how="cross")
print(df_cross)
print("\n")
