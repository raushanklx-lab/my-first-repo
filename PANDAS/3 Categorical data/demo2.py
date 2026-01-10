# Create categorical DataFrame in pandas

import pandas as pd

df = pd.DataFrame({"cat1":list("pqrs"),"cat2":list("pqrp"),"cat3":list("prrr")}, dtype="category")

print("\nDataFrame:\n",df)
print("\nDatatype of each column:\n", df.dtypes)                 