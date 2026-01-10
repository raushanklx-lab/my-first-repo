# contains() method in Python Pandas

import pandas as pd

data = ["Jacob","Amit Diwan","TRENT","Nathan","MaRtIN"]
s = pd.Series(data)
print(s)

print("\n Does the Specific Value exist? : \n", s.str.contains('Amit'))