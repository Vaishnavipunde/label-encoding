# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 16:33:00 2023

@author: sai
"""

import pandas as pd


# Load the dataset 'animal_category.csv' into a DataFrame 'df'
df = pd.read_csv("C:/2-dataset/animal_category.csv")

# Display the DataFrame 
df
# Get the dimensions (number of rows and columns) of the DataFrame
df.shape
# Display the column names of the DataFrame
df.columns

# Dropping the 'Index' column from the DataFrame 'df'
df.drop(['Index'], axis=1)

# Creating dummy variables for categorical columns in the DataFrame 'df' using one-hot encoding
# It converts categorical variables into binary numerical columns.
df_new = pd.get_dummies(df)
df_new.shape

# Dropping columns 'Gender_Male' and 'Homly_Yes' from the DataFrame 'df_new'
df_new.drop(["Gender_Male", "Homly_Yes"], axis=1, inplace=True)
df_new.shape

# Renaming columns in the DataFrame 'df_new'
df_new.rename(columns={"Gender_Female": "Gender", "Homly_No": "Homly"}, inplace=True)

##########################################################################################

# perform above operations on ethnic dataset

df1=pd.read_csv("C:/2-dataset/ethnic.csv")
df1

df1.dtypes
df1.columns

df1.shape
df1.drop(["Sex"],axis=1,inplace=True)

df_new1=pd.get_dummies(df1)
df_new1.shape

df_new1.drop(["Department","Race"],axis=1,inplace=True)
df_new1.shape

df_new1.rename(columns={"CitizenDesc":"city","MaritalDesc":"status"},inplace=True)
df_new1

