# Select two columns in a pandas dataframe

import pandas as pd

data = {
    "Student" : ["Amit","John","Raushan","Steve","David"],
    "Rank" : [2, 3, 1, 4, 5],
    "Marks" : [95, 83, 99, 75, 37],
    "Roll" : ["S01","S02","S03","S04","S05"]
}

df = pd.DataFrame(data)

print("Student Records : \n", df)
print("\nSelect only two column: \n", df[["Student","Rank","Marks"]]) # we use double bog bracket[] for select two or more column

print("\nSelect only single column: \n", df["Marks"])

