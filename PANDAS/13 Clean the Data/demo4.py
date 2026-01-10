# Pandas df.fillna() method

import pandas as pd

df = pd.read_csv("C:\\Users\\hp\\OneDrive\\Desktop\\DemoRRRCSV.csv")
print("\nOur DataFrame: \n",df)

resDF = df.fillna(111)
print("\nNew DataFrame (After replacing NULL with a Specific Value\n", resDF.to_string())