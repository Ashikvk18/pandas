import pandas as pd
data1 = {
    "Name" : ["Amit", "Ashik", "Rakin", "ella", "emma", "Sarah", "akansha", "john", "jane", "bob", "alice"],
    "Age" : [10,20,30,40,50,60,70,80,90,100,110],
    "City" : ["Texas", "California", "London", "Paris", "Tokyo", "Berlin", "Madrid", "New York", "London", "Paris", "Tokyo"],
    "Salary" : [1000,200000,3000,4000,5000,6000,7000,8000,9000,10000,11000],
    "Performance Score" : [88, 99, 91, 49, 55, 66, 77, 88, 99, 10, 11]
}
print(data1)

print("\n")

df1 = pd.DataFrame(data1)
print(df1)