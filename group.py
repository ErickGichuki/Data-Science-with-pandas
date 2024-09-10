# Data Grouping and Aggregation
import pandas as pd
df=pd.read_csv('data.csv', delimiter='\t')

# print(df.info())

# Scenario 1
# Question: How many cities are there in each country? 
# Hint - Group by country and count cities
country_group = df.groupby(by="Country")["City"].count()
# print("Total: ", country_group)

# Scenario 2
# Question: What is the average population for each country in 2024?
# Hint - Group by country and calculate the avg population
avg_pop = df.groupby(by="Country")["Population (2024)"].mean()
# print("Avg population for each country: ", avg_pop)

# Scenario 3
# Question: What is the total growth rate for each country
# Hint - Group by country and calculate total growth rate
Total_growthrate = df.groupby(by="Country")["Growth Rate"].sum()
# print("Total Growth Rate: ", Total_growthrate)

# Scenario 4
# Question: What is the avg population for each combination of country and growth rate category in 2024
# group by country and growth rate then calculate the avg population
avg_pop_growth = df.groupby(by=["Country", "Growth Rate"])["Population (2024)"].mean().reset_index()
# print("Avg pop: ", avg_pop_growth)

# Scenario 5
# Question: What are the summary statistics (mean, min, sum and max) for the population in 2024 for each country?
# Group by country and get summary statistics for population
grouped_data = df.groupby(by="Country")["Population (2024)"].agg(["mean","min","sum","max"])
# print("summary_stats: ", grouped_data)


# Scenario 6
# Question: How many cities fall into each growth rate category within each country?
# Group by Country and population growth rate categories

def growth_category(growth):
    if growth > 0.02:
        return "High Growth Rate"
    elif growth > 0:
        return "Moderate Growth Rate"
    else:
        return "Negative Growth Rate"
    
df["Growth Category"] = df["Growth Rate"].apply(growth_category)
growth_count = df.groupby(by=["Country", "Growth Category"])["City"].count()
print("Cities: ", growth_count)
