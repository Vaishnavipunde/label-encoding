# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 08:51:02 2023

@author: sai
"""
# mostly label encoding is done for nominal data



import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Instantiate LabelEncoder
label = LabelEncoder()

# Read the dataset 'ethnic.csv' into a DataFrame 'df'
df = pd.read_csv("C:/2-dataset/ethnic.csv")


# We have Salaries and age column in numeric so make them at 0 and 1 position for further processing
df = df[["Salaries", "age", "Position", "State", "Zip", "Sex", "MaritalDesc", "CitizenDesc", "Department", "Race"]]

# Splitting data into X (features) and Y (target)
X = df.iloc[:, 0:9]  # Features
Y = df["Race"]  # Target variable


# Fit label encoder to columns
# Encoding categorical columns using LabelEncoder
X["Sex"] = label.fit_transform(X["Sex"])
X["MaritalDesc"] = label.fit_transform(X["MaritalDesc"])
X["State"] = label.fit_transform(X["State"])

# Encoding the target variable 'Race'
y = label.fit_transform(Y)

# Here y is in the form of series so convert into dataframe
y=pd.DataFrame(y)


# Concatenating the encoded feature set (X) and target variable (y) into a new DataFrame 'df_new'
df_new = pd.concat([X, y], axis=1)

# Renaming the encoded 'Race' column in the new DataFrame
df_new = df_new.rename(columns={0: "Race"})











