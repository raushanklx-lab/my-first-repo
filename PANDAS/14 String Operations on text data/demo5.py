# count() method in Python Pandas

import numpy as np
import pandas as pd

data = [np.nan ,"Amit Diwan","Trent","Nathan Lyon","MaRtIN", np.nan]
s = pd.Series(data)
print(s)

print("\n Count (non-empty): \n", s.count())