#attribute and Methods of pandas series

import pandas as pd

#series index
data = [10,20,40,80,100]
s = pd.Series(data, index=["A","B","C","D","E"])
print("\nSeries Index :",s.index)

print("\nSeries Summary:\n\n",s.info)