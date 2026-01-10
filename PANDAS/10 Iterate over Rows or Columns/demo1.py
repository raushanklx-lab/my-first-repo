# Pandas iterrows() to iterate over rows

import pandas as pd

data = {
    "Student" : ["Amit","John","Raushan","Steve","David"],
    "Rank" : [2, 3, 1, 4, 5],
    "Marks" : [95, 83, 99, 75, 37],
    "Roll" : ["S01","S02","S03","S04","S05"]
}

df = pd.DataFrame(data)
print("Student Records : \n", df)

for row in df.iterrows():
    print("\nIterate over rows: \n", row)