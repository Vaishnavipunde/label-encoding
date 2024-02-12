# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 08:30:00 2023

@author: sai
"""

import pandas as pd
from sklearn.preprocessing import OneHotEncoder

# Initialize OneHotEncoder
enc = OneHotEncoder()

# Read the dataset 'ethnic.csv' into a DataFrame 'df'
df = pd.read_csv("C:/2-dataset/ethnic.csv")


df.columns

#we have Salaries and age column in numeric so make them at 0 and 1 position for further processing
df=df[["Salaries","age","Position","State","Zip","Sex","MaritalDesc","CitizenDesc","Department","Race"]]

#we want only nominal and ordinal data so skip 0 and1 column and then apply onehotencoder for all rows and columns from 3
enc_df=pd.DataFrame(enc.fit_transform(df.iloc[:,2:]).toarray())






































