#attribute and Methods of pandas DataFrame
import pandas as pd

data = {
    "student":["Ayush","Raushan","Manish","Tim","Baby"],
    "marks":[95,99,95,86,75],
    "Roll":["S01","S02","S03","S04","S05"]
}

df = pd.DataFrame(data)

print("\ndata Type:\n",df.dtypes)
print("\nNumber of Dimension: ",df.ndim)
print("\nNumber of elements: ",df.size)
print("\nShape: ",df.shape)
print("\nIndex: ",df.index)
print("\nTranspose:\n\n",df.T)

print("\nThe First 5 rows:\n",df.head())
print("\nThe First 3 rows:\n",df.head(3))

print("\nlast 5 rows:\n",df.tail())
print("\nlast 2 rows:\n",df.tail(2))