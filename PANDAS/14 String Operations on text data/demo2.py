# upper() method in Python Pandas

import pandas as pd

data = ["Jacob","Amit","TRENT","Nathan","MaRtIN"]
s = pd.Series(data)
print(s)

print("\n Uppercase Data: \n", s.str.upper())