
import pandas as pd

# Load the dataset
df = pd.read_csv("Sample - Superstore.csv", encoding="cp1252")

print("Original rows:", len(df))
print("Missing values:", df.isnull().sum().sum())
print("Duplicate rows:", df.duplicated().sum())

# Remove duplicates
df = df.drop_duplicates()

# Remove extra spaces from text
for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].str.strip()

# Convert date columns
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

# Save cleaned data
df.to_csv("Cleaned_Superstore.csv", index=False)

print("Data cleaning completed!")
print("Cleaned rows:", len(df))
