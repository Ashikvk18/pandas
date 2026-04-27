import pandas as pd
data1 = {
    "Name" : ["Amit", None, "Ashik", "Rakin", "ella", "emma", "Sarah", "akansha", "john", "jane", "bob", "alice"],
    "Age" : [10, None, 20,30,40,50,60,70,80,90,100,110],
    "City" : ["Texas", None, "California", "London", "Paris", "Tokyo", "Berlin", "Madrid", "New York", "London", "Paris", "Tokyo"],
    "Salary" : [1000, None, 200000,3000,4000,5000,6000,7000,8000,9000,10000,11000],
    "Performance Score" : [88, None, 99, 91, 49, 45, 62, 97, 78, 83, 92, 51]
}
print(data1)
df = pd.DataFrame(data1)
grouped = df.groupby(["City", "Age"])["Salary"].sum()
print(grouped)