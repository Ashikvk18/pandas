import pandas as pd

df_Reg1 = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35]
})

df_Reg2 = pd.DataFrame({
    "Name": ["David", "Eve", "Frank"],
    "Age": [40, 45, 50]
})

print(df_Reg1)
print(df_Reg2)

df_concat = pd.concat([df_Reg1, df_Reg2], ignore_index=True)
print(df_concat)
