# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 16:43:34 2023

@author: sai
"""
import pandas as pd

# Read the 'ethnic.csv' dataset into a DataFrame named 'ethnic'
ethnic = pd.read_csv("c:/2-dataset/ethnic.csv")

# Display the columns present in the DataFrame 
ethnic.columns

# Drop unnecessary columns from the DataFrame 
ethnic.drop(["Employee_Name", "EmpId", "Zip"], axis=1, inplace=True)

# Get descriptive statistics for the DataFrame 'ethnic'
ethnic.describe

# Convert categorical columns into numerical representation using one-hot encoding
ethnic = pd.get_dummies(ethnic, drop_first=True)

#in dataframe there is a huge difference bet min salary and max salary so we have to normalize it
#normalization fun to normalize the data
def norm_func(i):
    x=(i-i.min())/(i.max()-i.min())
    return x

# Apply normalization function to the DataFrame 'ethnic' and store the normalized data in 'df_norm'
df_norm = norm_func(ethnic)

# now check min max salary after normalization
b=df_norm.describe()





