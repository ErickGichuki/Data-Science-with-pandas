import pandas as pd
data=pd.read_csv('unclean.csv', delimiter='\t')
# print(data.info())

print("Initial shape: ", data.shape)
print("Is null: ",data.isnull().sum())
print("Is duplicated: ", data.duplicated().sum())

# Handle missing values
data.replace("?", pd.NA, inplace=True)

# Dropped any with missing data
critical_cols = ["Company","Cpu","Memory","Ram","Gpu","OpSys","Weight","Price"]
data = data.dropna(subset=critical_cols)

# Drop duplicates
data = data.drop_duplicates()
# print("Cleaned data shape: ", data.shape)

# Standardize our columns(convert strings (objects) into numbers (float64 or int64))
data["Weight"] = data["Weight"].str.replace("kg", "", regex=False)
data["Weight"] = pd.to_numeric(data["Weight"], errors="coerce")

data["Price"] = pd.to_numeric(data["Price"], errors="coerce")

# Windows 10 -> Windows_10
data["OpSys"] = data["OpSys"].str.lower().str.replace(" ","_")
# print("Current data shape: ", data.shape)
# print(data.head())

# Extract CPU speed from the "Cpu" column
def extract_cpu(cpu_info):
    try:
        return float(cpu_info.split()[-1]) # 2.7Ghz -> 2.7
    except Exception as e:
        return None

# Create a new column in our data set for the new cpu data
data["Cpu_speed"] = data["Cpu"].apply(extract_cpu)
# print("Current data shape: ", data.shape)

# Standardize our memory
def convert_memory(memory):
    try:
        if "GB" in memory:
            return int(memory.replace("GB","")) * 1024 # MB
        elif "TB" in memory:
            return int(memory.replace("TB","")) * 1024 * 1024
    except Exception as e:
        return None
    
# New column
data["Memory_MB"] = data["Memory"].apply(convert_memory)

# Replace any Nan with the avg of that column
# fillna()
data['Weight'].fillna(data["Weight"].mean(), inplace=True)
data['Price'].fillna(data["Price"].mean(), inplace=True)
data['Cpu_speed'].fillna(data["Cpu_speed"].mean(), inplace=True)
data['Memory_MB'].fillna(data["Memory_MB"].mean(), inplace=True)

# Final testing

print("Final data shape: ", data.shape)
print(data.head())
print("Missing values in each column after cleaning: ",data.isnull().sum())
print("Number of duplicate rows after cleaning: ", data.duplicated().sum())
print("Data types: ",data.dtypes)