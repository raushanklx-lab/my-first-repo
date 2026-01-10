# Sort the pandas df in descending Order

import pandas  as pd

data = {
    "student":["Ayush","Raushan","Manish","Tim","Baby"],
    "marks":[95,99,95,86,75],
    "Roll":["S01","S02","S03","S04","S05"]
}

df = pd.DataFrame(data, index= ["A","B","C","D","E"])
print("Record DataFrame : \n",df)
print("\n ", df.sort_values("marks", ascending=False))
print("\n ", df.sort_values(by =["marks"], ascending=False))