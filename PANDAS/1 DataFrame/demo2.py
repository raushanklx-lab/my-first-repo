# Access a group of rows or columns in a pandas DataFrame

import pandas as pd

data = {
    "student":["Ayush","Raushan","Manish","Tim","Baby"],
    "marks":[95,99,95,86,75],
    "Roll":["S01","S02","S03","S04","S05"]
}

df = pd.DataFrame(data, index = ["student1","student2","student3","student4","student5"])
print(df)