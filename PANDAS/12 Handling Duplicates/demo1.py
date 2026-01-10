# Find duplicates in pd using duplicated in pd using  duplicated()

import pandas as pd

data = {
    "student":["Ayush","Raushan","Manish","Tim","Baby","Raushan"],
    "marks":[95,99,95,86,75,99],
    "Roll":["S01","S02","S03","S04","S05","S02"]
}

df = pd.DataFrame(data)
print(df)

res = df.duplicated()
print("\ndescribing Duplicates : \n", res)