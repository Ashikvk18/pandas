import pandas as pd

df = pd.read_csv("data.csv")
print(df.describe())


data1 = {
    "Name" : ["Amit", "Ashik", "Rakin", "ella", "emma", "Sarah", "akansha", "john", "jane", "bob", "alice"],
    "Age" : [10,20,30,40,50,60,70,80,90,100,110],
    "City" : ["Texas", "California", "London", "Paris", "Tokyo", "Berlin", "Madrid", "New York", "London", "Paris", "Tokyo"],
    "Salary" : [1000,200000,3000,4000,5000,6000,7000,8000,9000,10000,11000],
    "Performance Score" : [88, 99, 91, 49, 55, 66, 77, 88, 99, 10, 11]
}

df1 = pd.DataFrame(data1)
print("DataFrame:")
print(df1)
print("\nDescribe:") # Statistical summary
print(df1.describe())
print("\nInfo:") # Shows data types and memory usage
print(df1.info())

# difference between describe and info
# describe is used for numerical data
# info is used for all data types but the major difference is that info shows data types and memory usage and describe shows statistical summary in simple words that is easy to understand describe and info are used for different purposes they are : 
# describe is used for numerical data and info is used for all data types. Info shows data types and memory usage and describe shows statistical summary in simple words that is easy to understand