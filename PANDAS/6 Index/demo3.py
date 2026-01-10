# # indexing in pd using iloc

import pandas as pd

df = pd.read_csv("C:\\Users\\hp\\OneDrive\\Desktop\\DemoRRRCSV.csv", index_col="Student")
print("\n Our DataFrame:\n",df)

res = df.iloc[2]
print("\n value : \n",res)