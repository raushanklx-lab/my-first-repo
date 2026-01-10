# lower() method in Python Pandas

import pandas as pd

data = ["Jacob","Amit","TRENT","Nathan","MaRtIN"]
s = pd.Series(data)
print(s)

print("\n Lowercase Data: \n", s.str.lower())