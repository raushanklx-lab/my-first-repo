# indexing in pd using loc

import pandas as pd

df = pd.read_csv("C:\\Users\\hp\\OneDrive\\Desktop\\DemoRRRCSV.csv", index_col="Student")
print("\n Our DataFrame: \n", df)

res = df.loc["David"]
print("\n Loc Data : \n",res)