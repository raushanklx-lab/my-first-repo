# Indexing in pandas using the indexing operators []

import pandas as pd

df = pd.read_csv("C:\\Users\\hp\\OneDrive\\Desktop\\DemoRRRCSV.csv", index_col="Student")
print("\nDataFrame: \n",df)

res = df["Marks"]
print("\n",res)