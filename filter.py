import pandas as pd

# Create a DataFrame from the CSV file with the correct delimiter
df = pd.read_csv('data.csv', delimiter='\t')

# print(df.info())

# print(df.head(8))

# print(df.describe())

# Scenario 1
# Find cities with a population greater than 20 million
large_cities = df[df['Population (2024)'] > 20000000]
#print('cities larger than 20 million', large_cities)

# Scenario 2
# Find all the largest cities in Vietnam
vietnam = df[df['Country'] == 'Vietnam']
#print('Largest cities in Vietman', vietnam)

# Scenario 3
# Find cities in China that are growing in population in 2024(positive growth)
growing_cities_china = df[(df["Country"] == "China") & (df["Growth Rate"] > 0)]
#print('Growing cities in china', growing_cities_china)

# Scenario 4
# Calculate the total population of the largest cities in India
cities_india = df[df['Country'] == "India"]["Population (2024)"].sum()
#print('sum of largest in india', cities_india)

# Scenario 5
# Find cities experiencing a population decline and calculate their growth median
decline_median = df[df["Growth Rate"] < 0]["Growth Rate"].median()
#print("decline median cities: ", decline_median)

# Scenario 6
# Finding the growing cities in china and calculate the minimum population they had in 2023
min_pop_china = df[(df["Country"] == "China") & (df["Growth Rate"] > 0)]["Population (2023)"].min()
print("Minimum pop in china for 2023", min_pop_china)