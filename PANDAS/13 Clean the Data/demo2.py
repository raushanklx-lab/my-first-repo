# Pandas notnull() method

import pandas as pd

df = pd.read_csv("C:\\Users\\hp\\OneDrive\\Desktop\\DemoRRRCSV.csv")
print("\nOur DataFrame: \n",df)

resDF = df.notnull()
print("\nNew DataFrame\n", resDF.to_string())