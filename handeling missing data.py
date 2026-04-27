import pandas as pd
data1 = {
    "Name" : ["Amit", None, "Ashik", "Rakin", "ella", "emma", "Sarah", "akansha", "john", "jane", "bob", "alice"],
    "Age" : [10, None, 20,30,40,50,60,70,80,90,100,110],
    "City" : ["Texas", None, "California", "London", "Paris", "Tokyo", "Berlin", "Madrid", "New York", "London", "Paris", "Tokyo"],
    "Salary" : [1000, None, 200000,3000,4000,5000,6000,7000,8000,9000,10000,11000],
    "Performance Score" : [88, None, 99, 91, 49, 55, 66, 77, 88, 99, 10, 11]
}
print(data1)
df = pd.DataFrame(data1)
print(df)

print(df.isnull())
print("\n")
print(df.isnull().sum()) #count of null values in each column