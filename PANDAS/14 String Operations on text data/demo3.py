# title() method in Python Pandas

import pandas as pd

data = ["Jacob","Amit","TRENT","Nathan","MaRtIN"]
s = pd.Series(data)
print(s)

print("\n Camel case Data: \n", s.str.title())