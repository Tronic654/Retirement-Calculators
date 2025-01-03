import pandas as pd
import os
from pathlib import Path


#Read .csv file into dataframe
current_dir = Path.cwd()
print(current_dir)
filefolder = current_dir / "data"
filepath = filefolder / "Shiller_Raw_Data.csv"

df = pd.read_csv(filepath)

#remove unnamed colummns
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

print(df.head())
print(df.dtypes)

#remove non-numerical characters from the strings
df = df.replace({'%': '', ',': '', ' ': ''}, regex=True)  # Remove '%' symbol
df = df.astype(float)  # Convert all columns to float

#Divide the last three rows by 100 to turn them into percent values
df.iloc[:, -3:] = df.iloc[:, -3:] / 100

print(df.head(12))
print(df.dtypes)

#Date: add padding to the float and convert to a string
df["Date"] = df["Date"].apply(lambda x: f"{x:.2f}")
print(df.head(12))
#convert the date column to a readable date
df["Date"] = pd.to_datetime(df["Date"], format="%Y.%m")
print(df.head(12))
print(df.dtypes)

#Drop Date Fraction column
df = df.drop("Date Fraction", axis=1)
print("Complete")
print(df)

#remove NAN rows
df = df.dropna(how="all")
print(df)

filepath_write = filefolder / "Shiller_Cleaned_Data.csv"
df.to_csv(filepath_write, index=False)