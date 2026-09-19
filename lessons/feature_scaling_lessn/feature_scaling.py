
#!/usr/bin/env python
# coding: utf-8

import pandas as pd
from sklearn.preprocessing import StandardScaler


# Load dataset
df = pd.read_csv('../../datasets/500hits.csv', encoding='latin-1')

print(df.head())


# Remove unnecessary columns
df = df.drop(columns=['PLAYER', 'CS'])

print(df.info())
print(df.describe().round(3))


# Select features
X1 = df.iloc[:, 0:13]
X2 = df.iloc[:, 0:13]


# Standardize X1
scaler = StandardScaler()
X1 = scaler.fit_transform(X1)


# Convert back to DataFrame with column names
X1 = pd.DataFrame(
    X1,
    columns=[
        'YRS', 'G', 'AB', 'R', 'H',
        '2B', '3B', 'HR', 'RBI', 'BB',
        'SO', 'SB', 'BA'
    ]
)

print(X1.head())