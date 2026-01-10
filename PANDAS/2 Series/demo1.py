#create a pandas series

import pandas as pd

data = [10,20,40,80,100]
s = pd.Series(data)
print("Series:\n",s)

#access a value
print("\nvalue from a pandas series:\n",s[3])

