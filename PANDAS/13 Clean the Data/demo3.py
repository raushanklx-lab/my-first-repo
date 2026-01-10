# Pandas df.dropna() method

import pandas as pd

df = pd.read_csv("C:\\Users\\hp\\OneDrive\\Desktop\\DemoRRRCSV.csv")
print("\nOur DataFrame: \n",df)

resDF = df.dropna()
print("\nNew DataFrame (After removing rows with NULL\n", resDF.to_string())